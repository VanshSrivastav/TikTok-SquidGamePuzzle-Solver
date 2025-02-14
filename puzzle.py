
class Node:
    def __init__(self, x,y, constraint = None, heuristic = None):
        '''
        x = x coord
        y = y coord
        constraint = move constraint (have to reach node at move count == constraint otherwise it is not a valid solution)
        heuristic, initialized as none so that I can dynamically assign heuristic values when computing whihc nodes to start from for each puzzle
        '''

        self.x = x
        self.y = y
        self.constraint = constraint
        self.heuristic = heuristic

    def set_constraint(self, constraint):
        self.constraint = constraint

    def get_constraint(self):
        return self.constraint


class Grid:
    
    def __init__(self, length, width, numMarkedNodes, moveConstraints):
        '''
        length = length of the grid to be generated
        width = width of the grid to be generated
        numMarkedNodes = number of constrained nodes to visit
        moveConstraints = set of unique move constraint values.
            each moveConstraint must meet these conditions:
                Cannot be larger than grid size
                Must be Unique
        '''
        self.length = length
        self.width = width
        self.numMarkedNodes = numMarkedNodes
        self.nodes = {}
        self.moveConstraints = set(moveConstraints)
        
        self.generate_grid()

    def get_grid(self):
        return list(self.nodes.keys())
    
    def str_rep(self):

        '''
        Returns a 2D grid matrix where each item in the grid is an array 
        which is a visual representation of the each node in the grid
        '''

        gridMatrix = []
        for i in range(self.length):
            row = []
            for j in range(self.width):
                if (i,j) in self.nodes:
                    node = [i,j,self.nodes[(i,j)].get_constraint()]
                    row.append(node)
                else:
                    row.append(None)
            gridMatrix.append(row)
        return gridMatrix


    def get_length(self):
        return self.length

    def get_width(self):
        return self.width
    
    def get_constraints(self):
        return self.moveConstraints
    
  
    def generate_grid(self):
        '''
        populates the nodes dictioary with node objects mapped to (x,y) coord tuple
        '''

        for i in range(self.length):
            for j in range(self.width):
                newNode = Node(i,j)
                self.nodes[(i,j)] = newNode

    
    def assign_mark(self,x,y,constraint):
        '''
        assigns constraint number to specified coords
        '''
        if (x,y) in self.nodes:
            self.nodes[(x,y)].set_constraint(constraint)
        else:
            print("Cannot assign node, this is out of bounds")

    def get_neighbors(self, x,y):
        '''
        inputs coord values, returns an array of neighbors
        '''
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)] 
        neighbors = []
        for dx, dy in directions:
            nx, ny = x + dx, y+dy
            if (nx,ny) in self.nodes:
                neighbors.append(self.nodes[(nx, ny)])

        return neighbors


            

        