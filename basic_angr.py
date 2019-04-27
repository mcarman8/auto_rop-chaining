import angr
import monkeyhex
proj = angr.Project('/bin/ssh')
block = proj.factory.block(proj.entry) #Get the block at the entry point
block.pp() #Pretty Print the block
print(block.instruction_addrs)
