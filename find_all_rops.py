import angr
import monkeyhex
import sys
from StringIO import StringIO

def create_rops(proj,instruction_addrs,all_rops_file):
    for i in range (1,12):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        block = proj.factory.block(instruction_addrs[-1]-i)
        block.pp()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        if "ret" in result_string:
            all_rops_file.write(result_string)
            all_rops_file.write("\n--------------------------------------------------------------------------\n")



proj = angr.Project('./0330_crackme_cpp/linux_x64/crackme_101')
cfg = proj.analyses.CFGFast()
print("here")
entry_func = cfg.kb.functions[proj.entry]
items = proj.kb.functions.items()
all_rops_file = open("./all_rops.txt","w+")
for item in items:
    block = proj.factory.block(item[0])
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result
    block.pp()
    sys.stdout = old_stdout
    result_string = result.getvalue()
    if "ret" in result_string:
        create_rops(proj,block.instruction_addrs,all_rops_file)

#for item in items:
#    sys.stdout = open("./functions/func_"+str(item[0]),"w+")
#    block = proj.factory.block(item[0])
#    block.pp()
#    print(block.instruction_addrs)
