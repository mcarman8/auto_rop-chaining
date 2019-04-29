import angr
import monkeyhex
import sys
from StringIO import StringIO

proj = angr.Project('./0330_crackme_cpp/linux_x64/crackme_101')
cfg = proj.analyses.CFGFast()
entry_func = cfg.kb.functions[proj.entry]
items = proj.kb.functions.items()
sys.stdou = open("./testfile.txt","w+")
for i in range (1,12):
    block = proj.factory.block(17377466-i)
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result
    block.pp()
    sys.stdout = old_stdout
    result_string = result.getvalue()
    if "ret" in result_string:
        print(result_string)
        print("--------------------------------------------------------------------------")
#for item in items:
#    sys.stdout = open("./functions/func_"+str(item[0]),"w+")
#    block = proj.factory.block(item[0])
#    block.pp()
#    print(block.instruction_addrs)
