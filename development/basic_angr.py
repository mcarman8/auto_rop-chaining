import angr
import monkeyhex
import sys
proj = angr.Project('./0330_crackme_cpp/linux_x64/crackme_101')
cfg = proj.analyses.CFGFast()
entry_func = cfg.kb.functions[proj.entry]
items = proj.kb.functions.items()
for item in items:
    sys.stdout = open("./functions/func_"+str(item[0]),"w+")
    block = proj.factory.block(item[0])
    block.pp()
    print(block.instruction_addrs)
