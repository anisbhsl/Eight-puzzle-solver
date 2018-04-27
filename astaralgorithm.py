# 8 Puzzle Solver using A* Algorithm in Python

import math, random

class puzzle:
	def __init__(self,start):  
		self.fronts=[]  #will act as a 2D list of frindges or frontier
		self.goalNode=['0','1','2','3','4','5','6','7','8']  #our goal node
		self.startNode=start  #initializing the puzzle 
		self.previousNode=[]  #will keep track of expanded nodes 


	# Heuristic Function
	def heuristic(self,node):
		hMisplaced=0
		hDist=0

		for i in range(9):
			if node[i]!=self.goalNode[i]:
				hMisplaced+=1
		for i in node:
			hDist+=math.fabs(node.index(i)-self.GoalNode.index(i))  # Manhatton distance 

		totalH=hMisplaced+hDist  # total heuristic value

		node.append(totalH)

		return node

	#shuffle the tiles

	def shuffle(self,node=[]):
		subNode=[]
		zeroLocation=node.index('0')+1
		subNode.extend(node)
		boundry=self.boundries(zeroLocation)
		self.fronts=[]

		if zeroLocation+3<=9:
			tmp=subNode[node.index('0')]
			subNode[node.index['0']]=subNode[node.index('0')+3]
			subNode[node.index('0')+3]=tmp
			self.fronts.append(self.heuristic(subNode))
			subNode=[]
			subNode.extend(node)
			print("UP ")
		if zeroLocation-3>=1:
			tmp=subNode[node.index('0')]
			subNode[node.index['0']]=subNode[node.index('0')-3]
			subNode[node.index('0')-3]=tmp
			self.fronts.append(self.heuristic(subNode))
			subNode=[]
			subNode.extend(node)
			print("DOWN ")

		if zeroLocation-1>=boundry[0]:
			tmp=subNode[node.index('0')]
			subNode[node.index['0']]=subNode[node.index('0')-1]
			subNode[node.index('0')-1]=tmp
			self.fronts.append(self.heuristic(subNode))
			subNode=[]
			subNode.extend(node)
			print("LEFT ")

	    if zeroLocation+1>=boundry[1]:
			tmp=subNode[node.index('0')]
			subNode[node.index['0']]=subNode[node.index('0')+1]
			subNode[node.index('0')+1]=tmp
			self.fronts.append(self.heuristic(subNode))
			subNode=[]
			subNode.extend(node)
			print("RIGHT ")

	#choose the next node
	# the node with miniumum heuristic value will be choosen
	def getNextNode(self):
		nextNode=[]
		tNode=[]

		while True:
			hrCost=100000
			for i in self.fronts:
				if(i[-1]<hrCost):
					hrCost=i[-1]   #update hrCost to the last element value
					nextNode=i[0:-1]  #update the list of nextNode
					tNode=i  #copy list with heuristic value

			if tNode in self.previousNode and tNode in self.fronts:
				self.fronts.remove(tNode) 
				self.previousNode.append(tNode)

			else:
				self.previousNode.append(tNode)
				return nextNode






