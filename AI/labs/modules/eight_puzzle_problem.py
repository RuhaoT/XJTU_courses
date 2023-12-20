from . import shared,EPP_BFS,EPP_Astar


def EPP_check_input_sequence(input):
    # check if the input is a string
    if not isinstance(input,str):
        return False
    # check if the input is 9 characters long
    if len(input) != 9:
        return False
    # check if the input contains only digits
    if not input.isdigit():
        return False
    # check if the input contains all digits from 0 to 8
    for i in range(9):
        if str(i) not in input:
            return False
    
    return True

def EPP_check_algorithm(algorithm):
    # check if the algorithm is a string
    if not isinstance(algorithm,str):
        return False
    # check if the algorithm is in the algorithm list
    if algorithm not in shared.EPP_algorithm_list:
        return False
    
    return True

def EPP_solve(input,target,algorithm,maxStep):
    # output variables
    status = "Invalid Input"
    state_space_tree = []
    solving_time = 0
    number_of_nodes_expanded = 0
    number_of_nodes_generated = 0
    max_depth_reached = 0

    # step 1: check if the input is valid
    is_valid = EPP_check_input_sequence(input) and EPP_check_input_sequence(target) and EPP_check_algorithm(algorithm)

    # step 2: if the input is valid, solve the problem
    if is_valid:
        status = "Solving"
        yield [status,state_space_tree,solving_time,number_of_nodes_expanded,number_of_nodes_generated,max_depth_reached]

        # BFS algorithm
        if algorithm == "BFS":
            # create a BFS object
            bfs = EPP_BFS.EPP_BFS(input,target,int(maxStep))
            # solve the problem
            bfs.solve()
            # record the solution
            if bfs.hasSolution:
                status = "Solved"
                state_space_tree = bfs.print_solution()
            else:
                status = "No Solution Found"
            
            solving_time = bfs.solvingTime
            number_of_nodes_expanded = bfs.numberOfNodesExpanded
            number_of_nodes_generated = bfs.numberOfNodesGenerated
            max_depth_reached = bfs.maxDepthReached
        
        # Astar algorithm
        if algorithm == "A* with misplaced tiles" or algorithm == "A* with Manhattan distance" or algorithm == "A* with Euclidean distance":
            # create a Astar object
            if algorithm == "A* with misplaced tiles":
                astar = EPP_Astar.EPP_Astar(input,target,int(maxStep),"misplaced tiles")
            elif algorithm == "A* with Manhattan distance":
                astar = EPP_Astar.EPP_Astar(input,target,int(maxStep),"manhattan distance")
            else:
                astar = EPP_Astar.EPP_Astar(input,target,int(maxStep),"euclidean distance")
            # solve the problem
            astar.solve()
            # record the solution
            if astar.hasSolution:
                status = "Solved"
                state_space_tree = astar.print_solution()
            else:
                status = "No Solution Found"
            
            solving_time = astar.solvingTime
            number_of_nodes_expanded = astar.numberOfNodesExpanded
            number_of_nodes_generated = astar.numberOfNodesGenerated
            max_depth_reached = astar.maxDepthReached


    yield [status,state_space_tree,solving_time,number_of_nodes_expanded,number_of_nodes_generated,max_depth_reached]

