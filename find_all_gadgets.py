# A tool that finds all possible gadgets in a binary
# Matthew Chorney and Mark Carman
# 04/28/19

import angr
import monkeyhex
import sys
from StringIO import StringIO
import argparse

def create_gadgets(proj,instruction_addrs,all_gadgets_file):
    for i in range (1,12):
        old_stdout = sys.stdout
        result = StringIO()
        sys.stdout = result
        block = proj.factory.block(instruction_addrs[-1]-i)
        block.pp()
        sys.stdout = old_stdout
        result_string = result.getvalue()
        if "ret" in result_string:
            all_gadgets_file.write(result_string)
            all_gadgets_file.write("\n--------------------------------------------------------------------------\n")


parser = argparse.ArgumentParser()
parser.add_argument("file")
args = parser.parse_args()
proj = angr.Project(args.file)
cfg = proj.analyses.CFGFast()
entry_func = cfg.kb.functions[proj.entry]
items = proj.kb.functions.items()
all_gadgets_file = open("./all_gadgets.txt","w+")
for item in items:
    block = proj.factory.block(item[0])
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result
    block.pp()
    sys.stdout = old_stdout
    result_string = result.getvalue()
    if "ret" in result_string:
        create_gadgets(proj,block.instruction_addrs,all_gadgets_file)
