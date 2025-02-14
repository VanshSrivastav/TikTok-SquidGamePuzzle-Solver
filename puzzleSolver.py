def AStar(graph, startNode, goalNode):
    pass



def solver(graph, startNode, goalNodeSet, traversalPath=None, goalNode=None):
    if traversalPath is None:
        traversalPath = []

    # Base case: If the entire graph is empty, all nodes have been explored
    if not graph:
        return True, traversalPath

    # If no valid start node exists, return failure
    if startNode is None:
        return False, traversalPath

    # If no goal node is assigned, take the first marked square as the goal
    if goalNode is None and goalNodeSet:
        goalNode = goalNodeSet[0]

    # Run A* search to get path from startNode to goalNode
    completed, newGraph, path = AStar(graph, startNode, goalNode)

    if completed:
        traversalPath.append(path)
        goalNodeSet.remove(goalNode)  # Remove the goal from set

        if goalNodeSet:
            nextGoal = goalNodeSet[0]  # Assign next goal node
            solved, path = solver(newGraph, goalNode, goalNodeSet, traversalPath, nextGoal)
        else:
            # Check if the grid is fully traversable from the last goal position
            solved, path = solver(newGraph, goalNode, goalNodeSet, traversalPath, None)

        return solved, path
    else:
        # A* failed to reach the goal; return failure
        return False, traversalPath
    

    # NEXT STEPS IMPLEMENT ASTAR AND THEN TEST VARIOUS PUZZLE SETS AND THEN DO THE TIKTOK ONE



