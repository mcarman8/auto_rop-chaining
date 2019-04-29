# A tool that finds all possible gadgets in a binary
# Matthew Chorney and Mark Carman
# 04/28/19

import angr
import monkeyhex
import sys
from StringIO import StringIO
import argparse

#This function generates the gadgets from a return location
def create_gadgets(proj,instruction_addrs,all_gadgets_file,the_range):
    for i in range (1,the_range):
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

#This gets the arguments
parser = argparse.ArgumentParser()
parser.add_argument("file",help="The file in which you want to find ROP gadgets")
parser.add_argument("-n",type=int,help="Number of bytes to use to generate intermediate gadgets. Default is 12",default=12)
args = parser.parse_args()
#set up the angr project
proj = angr.Project(args.file)
cfg = proj.analyses.CFGFast()
entry_func = cfg.kb.functions[proj.entry]
items = proj.kb.functions.items()
#File for output
all_gadgets_file = open("./all_gadgets.txt","w+")
#for every section that angr creates
for item in items:
    block = proj.factory.block(item[0])
    old_stdout = sys.stdout
    result = StringIO()
    sys.stdout = result
    block.pp()
    sys.stdout = old_stdout
    result_string = result.getvalue()
    #If there is a return, we can generate rop gadgets
    if "ret" in result_string:
        create_gadgets(proj,block.instruction_addrs,all_gadgets_file,args.n)
