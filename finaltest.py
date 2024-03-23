
final_branches =  {u'FileScannerService/feature/initial_code_sprint0': -740, u'FileScannerServiceV2/initial_checkin_1': -581, u'FileScannerServiceV2/feature/LoggingChanges_Scheguri_FB': -298, u'FileScannerServiceV2/dev': -298, u'FileScannerService/dev': -740, u'FileScannerServiceV2/master': -4, u'FileScannerServiceV2-SCTest/dev': -644, u'FileScannerService/master': -762, u'FileScannerServiceV2-SCTest/master': -644}
def filtered_branches (dict_final_branch):
    filtered_branch = {}
    for branch in dict_final_branch.keys():
        #if (("/feature/"  not in branch) and ("/master" not in branch) and ("/hotfix" not in branch)):
        if ("/feature/" in branch):
            filtered_branch[branch] = dict_final_branch[branch]
    return filtered_branch

final_branch = (filtered_branches(final_branches))
print (final_branch)
github_api_repo_url = "https://git01.pfsfhq.com/api/v3/repos/ISApps/"
for i in final_branch.keys():
    urlinfo = i.split('/',1)
    project_name = urlinfo[1]
    branch_name = urlinfo[1]
    print (github_api_repo_url+"/"+project_name+"/git/refs/heads/"+branch_name)
#test webhook


