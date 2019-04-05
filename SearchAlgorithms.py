class Node:
    id = None  # Unique value for each node.
    up = None  # Represents value of neighbors (up, down, left, right).
    down = None
    left = None
    right = None
    previousNode = None  # Represents value of neighbors.
    edgeCost = None  # Represents the cost on the edge from any parent to this node.
    gOfN = None  # Represents the total edge cost
    hOfN = None  # Represents the heuristic value
    heuristicFn = None  # Represents the value of heuristic function

    def __init__(self, value):
        self.value = value


class SearchAlgorithms:
    ''' * DON'T change Class, Function or Parameters Names and Order
        * You can add ANY extra functions,
          classes you need as long as the main
          structure is left as is '''
    path = []  # Represents the correct path from start node to the goal node.
    fullPath = []  # Represents all visited nodes from the start node to the goal node.
    totalCost = -1  # Represents the total cost in case using UCS, AStar (Euclidean or Manhattan)
    maze = []
    board = None

    def __init__(self, mazeStr, edgeCost=None):
        ''' mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node'''

        rows = mazeStr.split(' ')
        board = []
        c = rows[0].split(',')
        maze = []
        for i in range(len(rows)):
            cols = rows[i].split(',')
            for j in range(len(cols)):
                maze.append(cols[j])

        index = 0
        for i in range(len(rows)):
            board.append([])
            for j in range(len(cols)):
                node = Node(maze[index])
                node.id = index
                board[i].append(node)
                index += 1

        self.rows = rows;
        self.cols = cols;
        self.board = board;
        for i in range(len(self.rows)):
            for j in range(len(self.cols)):
                if i == 0:
                    if j == 0:
                        self.board[i][j].up = None
                        self.board[i][j].down = self.board[i + 1][j].value
                        self.board[i][j].left = None
                        self.board[i][j].right = self.board[i][j + 1].value

                    elif j == (len(self.cols) - 1):
                        self.board[i][j].up = None
                        self.board[i][j].down = self.board[i + 1][j].value
                        self.board[i][j].left = self.board[i][j - 1].value
                        self.board[i][j].right = None

                    else:
                        self.board[i][j].up = None
                        self.board[i][j].down = self.board[i + 1][j].value
                        self.board[i][j].left = self.board[i][j - 1].value
                        self.board[i][j].right = self.board[i][j + 1].value

                elif i == (len(self.rows) - 1):
                    if j == 0:
                        self.board[i][j].up = self.board[i - 1][j].value
                        self.board[i][j].down = None
                        self.board[i][j].left = None
                        self.board[i][j].right = self.board[i][j + 1].value

                    elif j == (len(self.cols) - 1):
                        self.board[i][j].up = self.board[i - 1][j].value
                        self.board[i][j].down = None
                        self.board[i][j].left = self.board[i][j - 1].value
                        self.board[i][j].right = None

                    else:
                        self.board[i][j].up = self.board[i - 1][j].value
                        self.board[i][j].down = None
                        self.board[i][j].left = self.board[i][j - 1].value
                        self.board[i][j].right = self.board[i][j + 1].value

                else:
                    if j == 0:
                        self.board[i][j].up = self.board[i - 1][j].value
                        self.board[i][j].down = self.board[i + 1][j].value
                        self.board[i][j].left = None
                        self.board[i][j].right = self.board[i][j + 1].value

                    elif j == (len(self.cols) - 1):
                        self.board[i][j].up = self.board[i - 1][j].value
                        self.board[i][j].down = self.board[i + 1][j].value
                        self.board[i][j].left = self.board[i][j - 1].value
                        self.board[i][j].right = None
                    else:
                        self.board[i][j].up = self.board[i - 1][j].value
                        self.board[i][j].down = self.board[i + 1][j].value
                        self.board[i][j].left = self.board[i][j - 1].value
                        self.board[i][j].right = self.board[i][j + 1].value

    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nod
        # es
        return self.path, self.fullPath
    
    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
    
        return self.path, self.fullPath
    
    #def get_adjecent(board):
    
    def UCS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost
    
    def AStarEuclideanHeuristic(self):
        # Cost for a step is calculated based on edge cost of node
        # and use Euclidean Heuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost
    
    def AStarManhattanHeuristic(self):
        # Cost for a step is 1
        # and use ManhattanHeuristic for evaluating the heuristic value
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        return self.path, self.fullPath, self.totalCost



def main():
    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.DFS()
    print('**DFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')

    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath = searchAlgo.BFS()
    print('**BFS**\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\n\n')
    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                  [0, 15, 2, 100, 60, 35, 30, 3
                                      , 100, 2, 15, 60, 100, 30, 2
                                      , 100, 2, 2, 2, 40, 30, 2, 2
                                      , 100, 100, 3, 15, 30, 100, 2
                                      , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.UCS()
    print('** UCS **\nPath is: ' + str(path) + '\nFull Path is: ' + str(fullPath) + '\nTotal Cost: ' + str(
        TotalCost) + '\n\n')
    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.',
                                  [0, 15, 2, 100, 60, 35, 30, 3
                                      , 100, 2, 15, 60, 100, 30, 2
                                      , 100, 2, 2, 2, 40, 30, 2, 2
                                      , 100, 100, 3, 15, 30, 100, 2
                                      , 100, 0, 2, 100, 30])
    path, fullPath, TotalCost = searchAlgo.AStarEuclideanHeuristic()
    print('**ASTAR with Euclidean Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')

    #######################################################################################

    searchAlgo = SearchAlgorithms('S,.,.,#,.,.,. .,#,.,.,.,#,. .,#,.,.,.,.,. .,.,#,#,.,.,. #,.,#,E,.,#,.')
    path, fullPath, TotalCost = searchAlgo.AStarManhattanHeuristic()
    print('**ASTAR with Manhattan Heuristic **\nPath is: ' + str(path) + '\nFull Path is: ' + str(
        fullPath) + '\nTotal Cost: ' + str(TotalCost) + '\n\n')


main()
