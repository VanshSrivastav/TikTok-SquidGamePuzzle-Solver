from puzzle import Node, Grid
import numpy as np

class PuzzleGenerator:

    def generate_puzzle(length, width, numMarkedNodes, moveConstraints):

        grid = Grid(length, width, numMarkedNodes,moveConstraints)
        
        return grid

    def randomGenerator(count):
            # Generate a set of random grid dimensions

        dimensions = list()
        numMarkedSquaresSet = list()

        problemSet = set() # this will store the puzzles we generate
        puzzleCount = count

        while len(dimensions) < puzzleCount: 
            length = np.random.randint(4, 6)
            width = np.random.randint(4, 6)
            dimensions.append((length, width)) 

        dimensions = list(dimensions)

        while len(numMarkedSquaresSet) < puzzleCount:
            gridSize = dimensions[np.random.randint(0, len(dimensions))]  # Select a grid size
            max_squares = gridSize[0] * gridSize[1]  # Max available spots in the grid
            numMarkedSquares = np.random.randint(1, max_squares + 1)  # Ensure within range
            numMarkedSquaresSet.append(numMarkedSquares)
        
        
        numMarkedSquaresSet = list(numMarkedSquaresSet)

        np.random.shuffle(dimensions)
        np.random.shuffle(numMarkedSquaresSet)

        for i in range(puzzleCount):
            gridSize = dimensions[i % len(dimensions)]  # Ensure we use available dimensions
            max_grid_size = gridSize[0] * gridSize[1]  # Total cells in the grid

            numMarkedSquareCount = numMarkedSquaresSet[i % len(numMarkedSquaresSet)]  # Get a valid count
            if numMarkedSquareCount > max_grid_size:
                continue  # Skip invalid configurations

            constraints = set()
            while len(constraints) < numMarkedSquareCount:
                constraint = np.random.randint(0, max_grid_size)  # Ensure within grid range
                constraints.add(constraint)

            if len(constraints) == numMarkedSquareCount:
                grid = PuzzleGenerator.generate_puzzle(gridSize[0], gridSize[1], numMarkedSquareCount, constraints)
                problemSet.add(grid)

        for problem in problemSet:
            constraints = list(problem.get_constraints())
            assigned_positions = set()
            
            while len(assigned_positions) < len(constraints):
                colPos = np.random.randint(0, problem.get_length())  
                rowPos = np.random.randint(0, problem.get_width())  
                
                # Ensure uniqueness
                if (colPos, rowPos) not in assigned_positions:
                    assigned_positions.add((colPos, rowPos))  # Mark as assigned
                    constraint_value = constraints[len(assigned_positions) - 1]  # Assign next constraint
                    problem.assign_mark(colPos, rowPos, constraint_value)  # Assign constraint to node


        # now wer have our puzzles generated WOOOOOO


        # optionally write puzzle to problems.txt we dont have to do this at all
        # but this is for visualization purposes (not very good visualization but whatever)

        with open('problems.txt','w') as file:
            for problem in problemSet:
                strRep = ''
                grid = problem.str_rep()
                for row in grid:
                    strRep+=''.join(str(row))
                    strRep+='\n'

                file.write(strRep)
            file.close()

        return problemSet

if __name__ == '__main__':

    problems = PuzzleGenerator.randomGenerator(1)
    print(problems)
    for problem in problems:
        gridMatrix = problem.str_rep()
        for row in gridMatrix:
            print(''.join(str(row)))
            print()

            
        
    # PUZZLE GENERATOR DONE
    # NEXT WE CODE A STAR AND TRAVERSE THESE GRAPHS, IF A STAR RETURNS A SOLUTION STORE THE GRAPH AS THE KEY AND THE RETURNED PATH AS A SOLUTION. 
    # 