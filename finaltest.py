
final_branches =  {u'FileScannerService/feature/initial_code_sprint0': -740, u'FileScannerServiceV2/initial_checkin_1': -581, u'FileScannerServiceV2/feature/LoggingChanges_Scheguri_FB': -298, u'FileScannerServiceV2/dev': -298, u'FileScannerService/dev': -740, u'FileScannerServiceV2/master': -4, u'FileScannerServiceV2-SCTest/dev': -644, u'FileScannerService/master': -762, u'FileScannerServiceV2-SCTest/master': -644}
def filtered_branches (dict_final_branch):
    filtered_branch = {}
    for branch in dict_final_branch.keys():
        #if (("/feature/"  not in branch) and ("/master" not in branch) and ("/hotfix" not in branch)):
        if ("/feature/" in branch):
            filtered_branch[branch] = dict_final_branch[branch]
    return filtered_branch

print (filtered_branches(final_branches))