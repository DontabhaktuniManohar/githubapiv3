#Author Name: Ramesh Bandavaram 
#Date: 15-Apr-2020
    
import requests
import json
import argparse
import sys
import csvtoHTML
from datetime import datetime
from dateutil import parser
from datetime import date
from requests.auth import HTTPBasicAuth
import os
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

try:
    os.remove("abc.txt")
except:
    print ("file not present")
orgs_url = "https://git01.pfsfhq.com/api/v3/orgs/"
repo_url = "https://git01.pfsfhq.com/api/v3/repos/"
def projectnames(repo_name):
    project_list = []
    for page in range (1,15):
        ret =  (requests.get(orgs_url+repo_name+"/repos?page="+str(page)+"&per_page=60&access_token=aa0d3eb79fcc2b08a4d16a3438d6e3715cccafd1",verify=False))
        json_res =  (ret.content)
        jsonres = json.loads(json_res)
        if  jsonres:
            lista = []
            #print (jsonres)
            for i in jsonres:
                print i['html_url']
                project_name =  i['html_url'].split('/')[-1]
                project_list.append(project_name)
    return project_list


#Branchnames
def getbranchnames(repo_name,project_list):
    branch_info = {}
    for project in project_list:
        branchnames_url = repo_url +repo_name+"/"+project+"/branches?access_token=aa0d3eb79fcc2b08a4d16a3438d6e3715cccafd1"
        ret_branches = requests.get(branchnames_url,verify=False)
        if (ret_branches.status_code == 200):
            ret_branches_res =  (ret_branches.content)
            retbranches = json.loads(ret_branches_res)
            for branch in retbranches:
                project_branch=project+"/"+branch['name']
                branch_info[project_branch]=branch['commit']['url']
    return branch_info

def last_commit_info(branch_info):
    br_commit_dt = {}
    for branch,commit_url in branch_info.items():
        res_branch_commit = requests.get(commit_url+"?access_token=aa0d3eb79fcc2b08a4d16a3438d6e3715cccafd1",verify=False)
        ret_last_commit =  (res_branch_commit.content)
        retcommitinfo = json.loads(ret_last_commit)
        commit_date = retcommitinfo['commit']['author']['date']
        str_commit_date = str(commit_date)
        br_commit_dt[branch]=commit_date
    return br_commit_dt

def numOfDays(date1, date2):
        return (date2-date1).days

def branchduration(br_commit_dt):
    branch_duration = {}
    for branch_name,commit_date in br_commit_dt.items():
        datetime_obj = parser.parse(commit_date)
        date__time = datetime_obj.strftime('%Y-%m-%d')
        get_cuurent_date =datetime.today().strftime('%Y-%m-%d')
        date_object1 = datetime.strptime(get_cuurent_date, '%Y-%m-%d').date()
        date_object2 = datetime.strptime(date__time, '%Y-%m-%d').date()
        diff_dance = numOfDays(date_object1,date_object2)
        branch_duration[branch_name] = diff_dance
    return branch_duration

def filtered_branches (dict_final_branch):
    filtered_branch = {}
    for branch in dict_final_branch.keys():
        if (("/release"  not in branch) and ("/master" not in branch) and ("/hotfix" not in branch)):
        #if ("/feature/" in branch):
            filtered_branch[branch] = dict_final_branch[branch]
    return filtered_branch

def write_to_file(content):
    with open("stalebrancheslist.csv",'a+') as file:
        file.write(content+"\n")


def deletebranch(repo_name,final_branch):
    github_api_repo_url = repo_url+repo_name
    print github_api_repo_url
    content_str = ""
    delete_urllist = {}
    for url,days in final_branch.items():
        urlinfo = url.split('/',1)
        project_name = urlinfo[0]
        branch_name = urlinfo[1]
        delete_url = (github_api_repo_url+"/"+project_name+"/git/refs/heads/"+branch_name)
        content_str = repo_name+","+project_name+","+branch_name+","+str(days)
        write_to_file(content_str)
        delete_urllist[delete_url]=days
    print (delete_urllist)

def main(argv):
    print (argv)
    parser = argparse.ArgumentParser()
    parser.add_argument('-o', '--org',  action="store", nargs="?",
                        help='provide organization value')
    if '-h' in argv or '--help' in argv:
        parser.print_help()
        sys.exit(0)
    args = parser.parse_args(argv)
    repo_name = args.org
    project_name=projectnames(repo_name)
    branch_list_names = getbranchnames(repo_name,project_name)
    print branch_list_names
    branch_commit_info_latest = last_commit_info(branch_list_names)
    print branch_commit_info_latest
    filtered_branchduration=branchduration(branch_commit_info_latest)
    final_branch = (filtered_branches(filtered_branchduration))
    print (final_branch)
    deletebranch(repo_name,final_branch)
    csvtoHTML.html_codeToHTML("stalebrancheslist.csv","reportfile.html")

if __name__ == '__main__':
    print "sys.argv=%s" % (sys.argv)
    main(sys.argv[1:    ])
