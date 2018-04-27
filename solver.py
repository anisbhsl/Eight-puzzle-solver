# 8 Puzzle Solver Implementation in Python

from astaralgorithm import *   

print ("--------------8 PUZZLE SOLVER-------------------\n")

#################### Input ###########################################

#puz=puzzle(startNode)
startNode=['1','0','2','3','4','5','6','7','8']
puz=puzzle(startNode)
if(startNode!=puz.goalNode):
	puz.shuffle(puz.startNode)
	nextNode=puz.getNextNode()
	

	while (nextNode!=puz.goalNode):
		puz.shuffle(nextNode)
		nextNode=puz.getNextNode()


	for i in nextNode:
		print(i,end=',')

else:
	print ("The start state is same as goal state")	


