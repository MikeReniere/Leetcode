from typing import Optional
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        
        def dfs(root): # this returns 2 values, boolean (if balanced), and height of the current subtree
            if not root:
                return [True, 0]
            left, right = dfs(root.left), dfs(root.right) # this checks if balanced from left and right nodes
            # if left[0] and right[0]:
            # checks if left and right are balanced, and if its  balanced from the root
            balanced = (left[0] and right[0] and abs(left[1] - right[1]) <= 1) 

            return [balanced, 1 + max(left[1], right[1])]
        return dfs(root)[0]
    
   
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
isBalanced = solution.isBalanced(root)

print(isBalanced)