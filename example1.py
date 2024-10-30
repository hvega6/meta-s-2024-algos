#given the root of a binary tree, return the vertical order traversal of its nodes' values. if two nodes are in the same row and column, the order should be from left to right.

# 3
#9  20 
# 15  7

#output should be [9][3,15][20][7]

#    3
#  9   8
#4  01   7
#  5   2

#output should be: [4][9,5][3,0,1][8,2][7]

#using the bfs(breath first search) algorithm you have to queue

#the root node can be our origin 0 and adding or subtracting 1 going left or right

#you will have to create a variable for the min index and the max index

from collections import defaultdict, deque

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalOrder(root: TreeNode):
    if not root:
        return []

    # Dictionary to hold the vertical order traversal
    column_table = defaultdict(list)
    # Queue for BFS
    queue = deque([(root, 0)])  # (node, column_index)
    min_column = 0
    max_column = 0

    while queue:
        node, column = queue.popleft()
        if node is not None:
            column_table[column].append(node.val)
            min_column = min(min_column, column)
            max_column = max(max_column, column)
            queue.append((node.left, column - 1))  # Go left
            queue.append((node.right, column + 1))  # Go right

    # Extract the values from the column_table in order
    return [column_table[x] for x in range(min_column, max_column + 1)]