from collections import deque
import math
import time

# node class for Astar algorithm
class EPP_Astar_Node:
    def __init__(self,id,sequence,parentId,depth,cost):
        self.id = id
        self.sequence = sequence
        self.parentId = parentId
        self.depth = depth
        self.cost = cost

# Astar algorithm class
class EPP_Astar:
    def __init__(self,input,target,maxStep,heuristic):
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
        self.heuristic = heuristic

    def node_closed(self,sequence):
        for closedNode in self.closedQueue:
            if closedNode.sequence == sequence:
                return True
        return False
    
    def calculate_node_cost(self,node):
        # if heuristic is misplaced tiles
        if self.heuristic == "misplaced tiles":
            # calculate the number of misplaced tiles
            misplaced_tiles = 0
            for i in range(9):
                if node.sequence[i] != self.target[i] and node.sequence[i] != "0":
                    misplaced_tiles += 1
            # calculate the cost
            node.cost = node.depth + misplaced_tiles
        # else if heuristic is manhattan distance
        elif self.heuristic == "manhattan distance":
            # calculate the manhattan distance
            manhattan_distance = 0
            # calculate distance for each tile
            for i in range(9):
                # if the tile is not empty
                if node.sequence[i] != "0":
                    # calculate the distance
                    current_row = i // 3
                    current_column = i % 3
                    target_row = self.target.index(node.sequence[i]) // 3
                    target_column = self.target.index(node.sequence[i]) % 3
                    manhattan_distance += abs(current_row - target_row) + abs(current_column - target_column)
            # calculate the cost
            node.cost = node.depth + manhattan_distance
        # else use euclidean distance
        else:
            # calculate the euclidean distance
            euclidean_distance = 0
            # calculate distance for each tile
            for i in range(9):
                # if the tile is not empty
                if node.sequence[i] != "0":
                    # calculate the distance
                    current_row = i // 3
                    current_column = i % 3
                    target_row = self.target.index(node.sequence[i]) // 3
                    target_column = self.target.index(node.sequence[i]) % 3
                    euclidean_distance += math.sqrt((current_row - target_row)**2 + (current_column - target_column)**2)
            # calculate the cost
            node.cost = node.depth + euclidean_distance
        return

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
            # if the child node is not in the closed queue, proceed
            if not self.node_closed(childSequence):
                # prepair child node id with number of node generated
                self.numberOfNodesGenerated += 1
                childId = self.numberOfNodesGenerated
                # create child node
                childNode = EPP_Astar_Node(childId,childSequence,node.id,node.depth+1,0)
                # calculate the cost
                self.calculate_node_cost(childNode)
                # add child node to open queue
                self.openQueue.append(childNode)

        # check if the empty tile can move down
        if emptyTileIndex < 6:
            hasChild = True
            # find the tile to exchange
            exchangeTileIndex = emptyTileIndex + 3
            # exchange the tiles
            childSequence = node.sequence[:emptyTileIndex] + node.sequence[exchangeTileIndex] + node.sequence[emptyTileIndex+1:exchangeTileIndex] + "0" + node.sequence[exchangeTileIndex+1:]
            # if the child node is not in the closed queue, proceed
            if not self.node_closed(childSequence):
                # prepair child node id with number of node generated
                self.numberOfNodesGenerated += 1
                childId = self.numberOfNodesGenerated
                # create child node
                childNode = EPP_Astar_Node(childId,childSequence,node.id,node.depth+1,0)
                # calculate the cost
                self.calculate_node_cost(childNode)
                # add child node to open queue
                self.openQueue.append(childNode)
        
        # check if the empty tile can move left
        if emptyTileIndex % 3 != 0:
            hasChild = True
            # find the tile to exchange
            exchangeTileIndex = emptyTileIndex - 1
            # exchange the tiles
            childSequence = node.sequence[:exchangeTileIndex] + "0" + node.sequence[exchangeTileIndex] + node.sequence[emptyTileIndex+1:]
            # if the child node is not in the closed queue, proceed
            if not self.node_closed(childSequence):
                # prepair child node id with number of node generated
                self.numberOfNodesGenerated += 1
                childId = self.numberOfNodesGenerated
                # create child node
                childNode = EPP_Astar_Node(childId,childSequence,node.id,node.depth+1,0)
                # calculate the cost
                self.calculate_node_cost(childNode)
                # add child node to open queue
                self.openQueue.append(childNode)
        
        # check if the empty tile can move right
        if emptyTileIndex % 3 != 2:
            hasChild = True
            # find the tile to exchange
            exchangeTileIndex = emptyTileIndex + 1
            # exchange the tiles
            childSequence = node.sequence[:emptyTileIndex] + node.sequence[exchangeTileIndex] + node.sequence[emptyTileIndex] + node.sequence[exchangeTileIndex+1:]
            # if the child node is not in the closed queue, proceed
            if not self.node_closed(childSequence):
                # prepair child node id with number of node generated
                self.numberOfNodesGenerated += 1
                childId = self.numberOfNodesGenerated
                # create child node
                childNode = EPP_Astar_Node(childId,childSequence,node.id,node.depth+1,0)
                # calculate the cost
                self.calculate_node_cost(childNode)
                # add child node to open queue
                self.openQueue.append(childNode)
        
        # Step 3: update max depth reached
        if node.depth+1 > self.maxDepthReached and hasChild:
            self.maxDepthReached = node.depth+1

        return

    def solve(self):
        # start timing
        startTime = time.time()

        # Step 1: initialize the open queue
        self.openQueue.append(EPP_Astar_Node(0,self.input,-1,0,0))

        # Step 2: while the open queue is not empty
        step = 0
        while len(self.openQueue) != 0:
            # check if the step exceeds the max step
            step += 1
            if step > self.maxStep:
                break

            # Step 2.1: reorder the open queue based on the cost
            self.openQueue = deque(sorted(self.openQueue,key=lambda node: node.cost))

            # Step 2.2: pop the first node from the open queue, which has the lowest cost
            currentNode = self.openQueue.popleft()

            # Step 2.3: add the current node to the closed queue
            self.closedQueue.append(currentNode)

            # Step 2.4: check if the current node is the target node
            if currentNode.sequence == self.target:
                self.hasSolution = True
                break

            # Step 2.5: expand the current node
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
                # find node with parent id
                for closedNode in self.closedQueue:
                    if closedNode.id == currentNode.parentId:
                        currentNode = closedNode
                        break
                self.solution.appendleft(currentNode)
        
        return
    
    def print_solution(self):
        solution_string = ""
        for node in self.solution:
            # obtain node sequence
            sequence = node.sequence
            # add sequence with middle bracket to solution string
            solution_string += "[[" + sequence[0:3] + "],[" + sequence[3:6] + "],[" + sequence[6:9] + "]]\n"
        return solution_string


