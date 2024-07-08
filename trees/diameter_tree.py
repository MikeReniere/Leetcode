from typing import Optional
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int: # returns the length p
        # diameter of example tree should be 4
        res  = [0]

        def dfs(root):
            if not root:
                return -1 # -1 is the height of a null tree
            left = dfs(root.left) # recursively run the dfs on both the subtrees of root 
            right = dfs(root.right) # left and right are the heights of each subtree

            res[0] = max(res[0],2 + left + right) # this is the diameter
            
            return 1 + max(left, right) # returns the max diameter that runs through the root node? 
        
        dfs(root)
        return res[0]



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
root = TreeNode(1)
root.left = TreeNode(2, TreeNode(4), TreeNode(5))
root.right = TreeNode(3, None, TreeNode(6))

solution.print_tree(root)
diameter = solution.diameterOfBinaryTree(root)

print(diameter)