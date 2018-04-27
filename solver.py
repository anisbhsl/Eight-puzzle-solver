# 8 Puzzle Solver Implementation in Python

from astaralgorithm import *   

print ("8 PUZZLE SOLVER")

#################### Input ###########################################

#puz=puzzle(startNode)
startNode=['0','1','2','3','4','5','6','7','8']
puz=puzzle(startNode)

puz.shuffle(puz.startNode)
nextNode=puz.getNextNode()


while (nextNode!=puz.goalNode):
	puz.shuffle(nextNode)
	nextNode=puz.getNextNode()


for i in nextNode:
	print(i,end=',')


