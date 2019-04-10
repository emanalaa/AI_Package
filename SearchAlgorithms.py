import collections
from queue import PriorityQueue
import math


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
    rows = []
    cols = []

    def __init__(self, mazeStr, edgeCost=None):
        """ mazeStr contains the full board
         The board is read row wise,
        the nodes are numbered 0-based starting
        the leftmost node"""

        rows = mazeStr.split(' ')
        board = []
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

        for i in range(len(rows)):
            for j in range(len(cols)):
                if i == 0:
                    if j == 0:
                        board[i][j].up = None
                        board[i][j].down = board[i + 1][j]
                        board[i][j].left = None
                        board[i][j].right = board[i][j + 1]

                    elif j == (len(cols) - 1):
                        board[i][j].up = None
                        board[i][j].down = board[i + 1][j]
                        board[i][j].left = board[i][j - 1]
                        board[i][j].right = None

                    else:
                        board[i][j].up = None
                        board[i][j].down = board[i + 1][j]
                        board[i][j].left = board[i][j - 1]
                        board[i][j].right = board[i][j + 1]

                elif i == (len(rows) - 1):
                    if j == 0:
                        board[i][j].up = board[i - 1][j]
                        board[i][j].down = None
                        board[i][j].left = None
                        board[i][j].right = board[i][j + 1]

                    elif j == (len(cols) - 1):
                        board[i][j].up = board[i - 1][j]
                        board[i][j].down = None
                        board[i][j].left = board[i][j - 1]
                        board[i][j].right = None

                    else:
                        board[i][j].up = board[i - 1][j]
                        board[i][j].down = None
                        board[i][j].left = board[i][j - 1]
                        board[i][j].right = board[i][j + 1]

                else:
                    if j == 0:
                        board[i][j].up = board[i - 1][j]
                        board[i][j].down = board[i + 1][j]
                        board[i][j].left = None
                        board[i][j].right = board[i][j + 1]

                    elif j == (len(cols) - 1):
                        board[i][j].up = board[i - 1][j]
                        board[i][j].down = board[i + 1][j]
                        board[i][j].left = board[i][j - 1]
                        board[i][j].right = None
                    else:
                        board[i][j].up = board[i - 1][j]
                        board[i][j].down = board[i + 1][j]
                        board[i][j].left = board[i][j - 1]
                        board[i][j].right = board[i][j + 1]

        self.rows = rows
        self.cols = cols
        self.board = board
        if not (edgeCost is None):
            x = 0
            for i in range(len(self.rows)):
                for j in range(len(self.cols)):
                    self.board[i][j].edgeCost = edgeCost[x]
                    x += 1

    def DFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nod
        # es
        rows_count = len(self.rows)
        columns_count = len(self.cols)

        visited = [0] * rows_count * columns_count
        stack = []

        for i in range(rows_count):
            for j in range(columns_count):
                if self.board[i][j].value == 'S':
                    stack.append(self.board[i][j])

        while len(stack) > 0:
            length = len(stack)
            current_node = stack[length - 1]
            visited[current_node.id] = 1
            self.fullPath.append(current_node.id)
            if current_node.up is not None and current_node.up.value != '#' and visited[current_node.up.id] == 0:
                current_node.up.previousNode = current_node
                if current_node.up.value == 'E':
                    self.fullPath.append(current_node.up.id)
                    self.path.append(current_node.up.id)
                    break
                elif current_node.up.value == '.':
                    stack.append(current_node.up)

            elif current_node.down is not None and current_node.down.value != '#' \
                    and visited[current_node.down.id] == 0:
                current_node.down.previousNode = current_node
                if current_node.down.value == 'E':
                    self.fullPath.append(current_node.down.id)
                    self.path.append(current_node.down.id)
                    break
                elif current_node.down.value == '.':
                    stack.append(current_node.down)

            elif current_node.left is not None and current_node.left.value != '#' \
                    and visited[current_node.left.id] == 0:
                current_node.left.previousNode = current_node
                if current_node.left.value == 'E':
                    self.fullPath.append(current_node.left.id)
                    self.path.append(current_node.left.id)
                    break
                elif current_node.left.value == '.':
                    stack.append(current_node.left)

            elif current_node.right is not None and current_node.right.value != '#' \
                    and visited[current_node.right.id] == 0:
                current_node.right.previousNode = current_node
                if current_node.right.value == 'E':
                    self.fullPath.append(current_node.right.id)
                    self.path.append(current_node.right.id)
                    break
                elif current_node.right.value == '.':
                    stack.append(current_node.right)
            else:
                stack.pop()
        while current_node.value != 'S':
            self.path.append(current_node.id)
            current_node = current_node.previousNode

        self.path.append(current_node.id)
        self.path.reverse()

        temp_list = []
        for i in range(len(self.fullPath)):
            if self.fullPath[i] not in temp_list:
                temp_list.append(self.fullPath[i])
        self.fullPath.clear()
        self.fullPath = temp_list
        return self.path, self.fullPath

    def BFS(self):
        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.fullPath.clear()
        self.path.clear()

        start = None
        end = None
        for i in range(len(self.rows)):
            for j in range(len(self.cols)):
                if self.board[i][j].value == 'S':
                    start = self.board[i][j]

                if self.board[i][j].value == 'E':
                    end = self.board[i][j]

        queue = [start]
        visited = set()

        while len(queue) != 0:
            front = queue.pop(0)
            visited.add(front.id)

            if front.id not in self.fullPath:
                self.fullPath.append(front.id)

            if front == end:
                end = front
                break

            up = None
            down = None
            right = None
            left = None

            for i in range(len(self.rows)):
                for j in range(len(self.cols)):
                    if self.board[i][j].id == front.id:
                        up = self.board[i][j].up
                        down = self.board[i][j].down
                        right = self.board[i][j].right
                        left = self.board[i][j].left

            if up is not None and up.value != '#' and up.id not in visited:
                queue.append(up)
                up.previousNode = front

            if down is not None and down.value != '#' and down.id not in visited:
                queue.append(down)
                down.previousNode = front

            if left is not None and left.value != '#' and left.id not in visited:
                queue.append(left)
                left.previousNode = front

            if right is not None and right.value != '#' and right.id not in visited:
                queue.append(right)
                right.previousNode = front

        # d = end
        # self.path.append(end.id)
        while end != start:
            self.path.append(end.id)
            end = end.previousNode
        self.path.append(end.id)
        self.path.reverse()

        return self.path, self.fullPath

    def UCS(self):

        # Fill the correct path in self.path
        # self.fullPath should contain the order of visited nodes
        self.fullPath.clear()
        self.path.clear()
        open_nodes = []  # not visited
        visited = []
        start = None
        end = None
        for i in range(len(self.rows)):  # searching for start node
            for j in range(len(self.cols)):
                if self.board[i][j].value == 'S':
                    start = self.board[i][j]
                    open_nodes.append(self.board[i][j])
                if self.board[i][j].value == 'E':
                    end = self.board[i][j]
                    break

        while len(open_nodes) > 0:
            node = min(open_nodes, key=lambda x: x.edgeCost)

            if node not in visited:
                visited.append(node)

            self.fullPath.append(node.id)

            if node.value == 'E':
                break

            else:

                if node.up is not None and node.up.value != '#':
                    node.up.previousNode = node

                    if node.up not in open_nodes and node.up not in visited:
                        open_nodes.append(node.up)
                        node.up.edgeCost = node.up.edgeCost + node.up.previousNode.edgeCost

                    else:
                        if node.up.edgeCost >= node.up.edgeCost + node.up.previousNode.edgeCost:
                            node.up.edgeCost = node.up.edgeCost + node.up.previousNode.edgeCost

                if node.down is not None and node.down.value != '#':
                    node.down.previousNode = node

                    if node.down not in open_nodes and node.down not in visited:
                        open_nodes.append(node.down)
                        node.down.edgeCost = node.down.edgeCost + node.down.previousNode.edgeCost

                    else:
                        if node.down.edgeCost >= node.down.edgeCost + node.down.previousNode.edgeCost:
                            node.down.edgeCost = node.down.edgeCost + node.down.previousNode.edgeCost

                if node.left is not None and node.left.value != '#':
                    node.left.previousNode = node

                    if node.left not in open_nodes and node.left not in visited:
                        open_nodes.append(node.left)
                        node.left.edgeCost = node.left.edgeCost + node.left.previousNode.edgeCost

                    else:
                        if node.left.edgeCost >= node.left.edgeCost + node.left.previousNode.edgeCost:
                            node.left.edgeCost = node.left.edgeCost + node.left.previousNode.edgeCost

                if node.right is not None and node.right.value != '#':
                    node.right.previousNode = node

                    if node.right not in open_nodes and node.right not in visited:
                        open_nodes.append(node.right)
                        node.right.edgeCost = node.right.edgeCost + node.right.previousNode.edgeCost

                    else:
                        if node.right.edgeCost >= node.right.edgeCost + node.right.previousNode.edgeCost:
                            node.right.edgeCost = node.right.edgeCost + node.right.previousNode.edgeCost

            open_nodes.remove(node)
        sz = len(visited)
        self.totalCost = visited[sz - 1].edgeCost
        ''' while end !=start:
            self.path.append(end.id)
            end =end.previousNode
        self.path.reverse()'''
        return [], self.fullPath, self.totalCost

    def AStarEuclideanHeuristic(self):

        self.fullPath.clear()
        self.path.clear()
        c = 0
        d = 0
        for i in range(len(self.rows)):  # searching for end node to save it to calculate H with all points
            for j in range(len(self.cols)):
                if self.board[i][j].value == 'E':
                    c = i
                    d = j
                    break
        for i in range(len(self.rows)):  # calculating HofN and edge cost  for each node
            for j in range(len(self.cols)):
                self.board[i][j].hOfN = math.sqrt((math.pow(abs(i - c), 2)) + math.pow(abs(j - d), 2))

        open_nodes = []  # not visited
        visited = []
        start = None
        end = None
        for i in range(len(self.rows)):  # searching for start node
            for j in range(len(self.cols)):
                if self.board[i][j].value == 'S':
                    start = self.board[i][j]
                    self.board[i][j].gOfN = 0
                    self.board[i][j].heuristicFn = self.board[i][j].hOfN
                    open_nodes.append(self.board[i][j])
                if self.board[i][j].value == 'E':
                    end = self.board[i][j]
                    break

        while len(open_nodes) > 0:
            node = min(open_nodes, key=lambda x: x.heuristicFn)

            if node not in visited:
                visited.append(node)

            self.fullPath.append(node.id)

            if node.value == 'E':
                self.totalCost = node.heuristicFn
                break

            else:

                if node.up is not None and node.up.value != '#':
                    node.up.previousNode = node

                    if node.up not in open_nodes and node.up not in visited:
                        open_nodes.append(node.up)
                        node.up.gOfN = node.up.previousNode.gOfN + node.up.edgeCost
                        node.up.heuristicFn = node.up.hOfN + node.up.gOfN

                    else:
                        if node.up.heuristicFn >= node.up.hOfN + (node.up.previousNode.gOfN + node.up.edgeCost):
                            node.up.heuristicFn = node.up.hOfN + (node.up.previousNode.gOfN + node.up.edgeCost)

                if node.down is not None and node.down.value != '#':
                    node.down.previousNode = node

                    if node.down not in open_nodes and node.down not in visited:
                        open_nodes.append(node.down)
                        node.down.gOfN = node.down.previousNode.gOfN + node.down.edgeCost
                        node.down.heuristicFn = node.down.hOfN + node.down.gOfN

                    else:
                        if node.down.heuristicFn >= node.down.hOfN + (node.down.previousNode.gOfN + node.down.edgeCost):
                            node.down.heuristicFn = node.down.hOfN + (node.down.previousNode.gOfN + node.down.edgeCost)

                if node.left is not None and node.left.value != '#':
                    node.left.previousNode = node

                    if node.left not in open_nodes and node.left not in visited:
                        open_nodes.append(node.left)
                        node.left.gOfN = node.left.previousNode.gOfN + node.left.edgeCost
                        node.left.heuristicFn = node.left.hOfN + node.left.gOfN

                    else:
                        if node.left.heuristicFn >= node.left.hOfN + (node.left.previousNode.gOfN + node.left.edgeCost):
                            node.left.heuristicFn = node.left.hOfN + (node.left.previousNode.gOfN + node.left.edgeCost)

                if node.right is not None and node.right.value != '#':
                    node.right.previousNode = node

                    if node.right not in open_nodes and node.right not in visited:
                        open_nodes.append(node.right)
                        node.right.gOfN = node.right.previousNode.gOfN + node.right.edgeCost
                        node.right.heuristicFn = node.right.hOfN + node.right.gOfN

                    else:
                        if node.right.heuristicFn >= node.right.hOfN + (
                                node.right.previousNode.gOfN + node.right.edgeCost):
                            node.right.heuristicFn = node.right.hOfN + (
                                    node.right.previousNode.gOfN + node.right.edgeCost)

            open_nodes.remove(node)
        return self.path, self.fullPath, self.totalCost

    def AStarManhattanHeuristic(self):

        self.fullPath.clear()
        self.path.clear()

        for i in range(len(self.rows)):  # searching for end node to save it to calculate H with all points
            for j in range(len(self.cols)):
                if self.board[i][j].value == 'E':
                    c = i
                    d = j
                    break
        for i in range(len(self.rows)):  # calculating HofN and edge cost  for each node
            for j in range(len(self.cols)):
                self.board[i][j].hOfN = abs(i - c) + abs(j - d)

        open_nodes = []  # not visited
        visited = []
        start = None
        end = None
        for i in range(len(self.rows)):  # searching for start node
            for j in range(len(self.cols)):
                if self.board[i][j].value == 'S':
                    start = self.board[i][j]
                    self.board[i][j].gOfN = 0
                    self.board[i][j].heuristicFn = self.board[i][j].hOfN
                    open_nodes.append(self.board[i][j])
                if self.board[i][j].value == 'E':
                    end = self.board[i][j]
                    break

        while len(open_nodes) > 0:
            node = min(open_nodes, key=lambda x: x.heuristicFn)

            if node not in visited:
                visited.append(node)

            self.fullPath.append(node.id)

            if node.value == 'E':
                self.totalCost = node.heuristicFn
                break

            else:

                if node.up is not None and node.up.value != '#':
                    node.up.previousNode = node

                    if node.up not in open_nodes and node.up not in visited:
                        open_nodes.append(node.up)
                        node.up.gOfN = node.up.previousNode.gOfN + 1
                        node.up.heuristicFn = node.up.hOfN + node.up.gOfN

                    else:
                        if node.up.heuristicFn >= node.up.hOfN + (node.up.previousNode.gOfN + 1):
                            node.up.heuristicFn = node.up.hOfN + (node.up.previousNode.gOfN + 1)

                if node.down is not None and node.down.value != '#':
                    node.down.previousNode = node

                    if node.down not in open_nodes and node.down not in visited:
                        open_nodes.append(node.down)
                        node.down.gOfN = node.down.previousNode.gOfN + 1
                        node.down.heuristicFn = node.down.hOfN + node.down.gOfN

                    else:
                        if node.down.heuristicFn >= node.down.hOfN + (node.down.previousNode.gOfN + 1):
                            node.down.heuristicFn = node.down.hOfN + (node.down.previousNode.gOfN + 1)

                if node.left is not None and node.left.value != '#':
                    node.left.previousNode = node

                    if node.left not in open_nodes and node.left not in visited:
                        open_nodes.append(node.left)
                        node.left.gOfN = node.left.previousNode.gOfN + 1
                        node.left.heuristicFn = node.left.hOfN + node.left.gOfN

                    else:
                        if node.left.heuristicFn >= node.left.hOfN + (node.left.previousNode.gOfN + 1):
                            node.left.heuristicFn = node.left.hOfN + (node.left.previousNode.gOfN + 1)

                if node.right is not None and node.right.value != '#':
                    node.right.previousNode = node

                    if node.right not in open_nodes and node.right not in visited:
                        open_nodes.append(node.right)
                        node.right.gOfN = node.right.previousNode.gOfN + 1
                        node.right.heuristicFn = node.right.hOfN + node.right.gOfN

                    else:
                        if node.right.heuristicFn >= node.right.hOfN + (node.right.previousNode.gOfN + 1):
                            node.right.heuristicFn = node.right.hOfN + (node.right.previousNode.gOfN + 1)

            open_nodes.remove(node)

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
