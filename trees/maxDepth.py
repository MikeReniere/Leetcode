from typing import Optional
from collections import deque
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class Solution:

    # recursive DFS

    # def maxDepth(self, root: Optional[TreeNode]) -> int:
    #     # recurive DFS (depth first Search) - goes to the bottom of every branch first 
    #     if not root:
    #         return 0
    #     return 1+max(self.maxDepth(root.left), self.maxDepth(root.right))
    

    # this is iterative BFS

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: # if its empty 
            return 0
        
        level = 0
        q = deque([root]) #deque is a double ended queue (list) - like a stack, can come out of either side 
        while q:

            for i in range(len(q)): #traverse a level, remove that level
                node = q.popleft()
                if node.left != None:
                    q.append(node.left)
                if node.right: 
                    q.append(node.right)
            level += 1
        return level
    

    def print_tree(self, node):
        if not node:
            return
        queue = [node]
        while queue:
            current = queue.pop(0)
            print(current.value, end=' ')
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
        print()
# Example usage:
# Creating a binary tree:
#        1
#       / \
#      2   3
#     / \   \
#    4   5   6
solution = Solution()
# root = TreeNode(1)
# root.left = TreeNode(2, TreeNode(4), TreeNode(5))
# root.right = TreeNode(3, None, TreeNode(6))


# Creating a binary tree:
#        3
#       / \
#      9   20
#         / \
#        15 7
root = TreeNode(3)
root.left = TreeNode(9, None, None)
root.right = TreeNode(20, TreeNode(15), TreeNode(7))

print(solution.maxDepth(root))
# solution.print_tree(root)
# invertedRoot = solution.invertTree(root)
# solution.print_tree(invertedRoot)