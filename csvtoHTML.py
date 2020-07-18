import copy
import os
class csvtoHTML(object):
    pass
def _init_():
    pass

def ConvertToHtml(csvreport):
    with open(csvreport, "r") as csvfile:
        lines = csvfile.readlines()
        #content = [x.strip() for x in content]

        b = []
        b.append('''
        <head>
        <style>
        table {
        border: 1px solid #ccc;
        border-radius: 10px;
        border-spacing: 0;
        }
        table td,
        table th {
        border-bottom: 1px solid #ccc;
        padding: 8px;
        }
        table tr:last-child > td {
        border-bottom: none;
        }
        </style>
        </head>
        <table>
        <tr>
        ''')
        b.append("<th> GIT_ORG </th> <th> REPO_NAME </th> <th> BRANCH_NAME </th> <th> LAST_COMMIT_DAYS </th> </tr>" + "\n")
        for line in lines:
            headerfields = line.split(",")
            for headers in headerfields:

                #if(lines.index(line) == 0):
                #    b.append("<th>"+headers.strip()+"</th>" + "\n")
                #else:
                b.append("<td align='center'>"+headers.strip()+"</td>"+ "\n")
            b.append("</tr>" + "\n")
        b.append('''
        </table>
        </body>
        </html>
        ''')
        c = "".join(b)
        return c

def html_codeToHTML(csvreport,reportfile):
    html_code = ConvertToHtml(csvreport)
    with open(reportfile,'w')as f:
       f.write(html_code)