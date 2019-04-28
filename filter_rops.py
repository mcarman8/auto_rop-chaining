import argparse

parser = argparse.ArgumentParser()
parser.add_argument("-r", "--register", type=str, help="A register to search for")
parser.add_argument("-i", "--instruction", type=str, help="An intruction to search for")
parser.add_argument("-l", "--line", type=str, help="A full line of intel assembly to search for")
parser.add_argument("-I", "--inFile", type=str, help="File to read input from")
parser.add_argument("-o", "--outFile", type=str, help="File to write output to")
args = parser.parse_args()
inFile = ""
outFile = ""
if args.inFile:
    inFile = args.inFile
else:
    inFile = "./all_rops.txt"
if args.outFile:
    outFile = args.outFile
else:
    outFile = "./filtered_rops.txt"
output = open(inFile, "r")
new = open(outFile, "w")
block = ""
args_used = []
if args.register:
    args_used.append(args.register)
if args.instruction:
    args_used.append(args.instruction)
if args.line:
    args_used.append(args.line)
for line in output:
    if "-----------------" in line:
        passed = True
        for filter in args_used:
            if not filter in block:
                block = ""
                passed = False
                break
        if passed:
            new.write(block)
            new.write("-----------------------------------------------------------------\n")
            block = ""
    else:
        block = block + line
new.write("\n")
output.close()
    
