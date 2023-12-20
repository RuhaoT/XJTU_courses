from collections import deque
import time

# node class for BFS algorithm
class EPP_BFS_Node:
    def __init__(self,id,sequence,parentId,depth):
        self.id = id
        self.sequence = sequence
        self.parentId = parentId
        self.depth = depth

# BFS algorithm class
class EPP_BFS:
    def __init__(self,input,target,maxStep):
        self.input = input
        self.target = target
        self.hasSolution = False
        self.solution = deque()
        self.solvingTime = 0
        self.numberOfNodesExpanded = 0
        self.numberOfNodesGenerated = 0
        self.maxDepthReached = 0
        self.openQueue = deque()
        self.closedQueue = deque()
        self.maxStep = maxStep

    def solve(self):
        # start timing
        startTime = time.time()

        # Step 1: initialize the open queue
        self.openQueue.append(EPP_BFS_Node(0,self.input,-1,0))

        # Step 2: while the open queue is not empty
        step = 0
        while len(self.openQueue) != 0:
            # check if the step exceeds the max step
            step += 1
            if step > self.maxStep:
                break

            # Step 2.1: pop the first node from the open queue
            currentNode = self.openQueue.popleft()
            # print("Checking node: " + str(currentNode.id) + " with sequence: " + currentNode.sequence)
            # input("Press Enter to continue...")

            # Step 2.2: add the current node to the closed queue
            self.closedQueue.append(currentNode)

            # Step 2.3: check if the current node is the target node
            if currentNode.sequence == self.target:
                self.hasSolution = True
                break

            # Step 2.4: expand the current node
            self.numberOfNodesExpanded += 1
            self.expand_node(currentNode)
        
        # end timing
        endTime = time.time()

        # calculate solving time
        self.solvingTime = endTime - startTime

        # record solution
        if self.hasSolution:
            self.solution.append(currentNode)
            while currentNode.parentId != -1:
                currentNode = self.closedQueue[currentNode.parentId]
                self.solution.appendleft(currentNode)


    def expand_node(self,node):
        # Step 1: find the empty tile
        emptyTileIndex = node.sequence.find("0")

        # Step 2: find and create all possible child nodes
        # check if the empty tile can move up
        if emptyTileIndex > 2:
            hasChild = True
            # find the tile to exchange
            exchangeTileIndex = emptyTileIndex - 3
            # exchange the tiles
            childSequence = node.sequence[:exchangeTileIndex] + "0" + node.sequence[exchangeTileIndex+1:emptyTileIndex] + node.sequence[exchangeTileIndex] + node.sequence[emptyTileIndex+1:]
            # prepair child node id with number of node generated
            self.numberOfNodesGenerated += 1
            childId = self.numberOfNodesGenerated
            # create child node
            childNode = EPP_BFS_Node(childId,childSequence,node.id,node.depth+1)
            # add child node to open queue
            self.openQueue.append(childNode)

        # check if the empty tile can move down
        if emptyTileIndex < 6:
            hasChild = True
            # find the tile to exchange
            exchangeTileIndex = emptyTileIndex + 3
            # exchange the tiles
            childSequence = node.sequence[:emptyTileIndex] + node.sequence[exchangeTileIndex] + node.sequence[emptyTileIndex+1:exchangeTileIndex] + "0" + node.sequence[exchangeTileIndex+1:]
            # prepair child node id with number of node generated
            self.numberOfNodesGenerated += 1
            childId = self.numberOfNodesGenerated
            # create child node
            childNode = EPP_BFS_Node(childId,childSequence,node.id,node.depth+1)
            # add child node to open queue
            self.openQueue.append(childNode)
        
        # check if the empty tile can move left
        if emptyTileIndex % 3 != 0:
            hasChild = True
            # find the tile to exchange
            exchangeTileIndex = emptyTileIndex - 1
            # exchange the tiles
            childSequence = node.sequence[:exchangeTileIndex] + "0" + node.sequence[exchangeTileIndex] + node.sequence[emptyTileIndex+1:]
            # prepair child node id with number of node generated
            self.numberOfNodesGenerated += 1
            childId = self.numberOfNodesGenerated
            # create child node
            childNode = EPP_BFS_Node(childId,childSequence,node.id,node.depth+1)
            # add child node to open queue
            self.openQueue.append(childNode)
        
        # check if the empty tile can move right
        if emptyTileIndex % 3 != 2:
            hasChild = True
            # find the tile to exchange
            exchangeTileIndex = emptyTileIndex + 1
            # exchange the tiles
            childSequence = node.sequence[:emptyTileIndex] + node.sequence[exchangeTileIndex] + node.sequence[emptyTileIndex] + node.sequence[exchangeTileIndex+1:]
            # prepair child node id with number of node generated
            self.numberOfNodesGenerated += 1
            childId = self.numberOfNodesGenerated
            # create child node
            childNode = EPP_BFS_Node(childId,childSequence,node.id,node.depth+1)
            # add child node to open queue
            self.openQueue.append(childNode)
        
        # Step 3: update max depth reached
        if node.depth+1 > self.maxDepthReached and hasChild:
            self.maxDepthReached = node.depth+1

        return
    
    def print_solution(self):
        solution_string = ""
        for node in self.solution:
            # obtain node sequence
            sequence = node.sequence
            # add sequence with middle bracket to solution string
            solution_string += "[[" + sequence[0:3] + "],[" + sequence[3:6] + "],[" + sequence[6:9] + "]]\n"
        return solution_string
            
        