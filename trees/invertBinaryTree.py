from typing import Optional
class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root: # if root is null
            return None
            
        # swap the children
        tmp = root.left
        root.left = root.right
        root.right = tmp

        # recursive call on the root stuff
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
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
invertedRoot = solution.invertTree(root)
solution.print_tree(invertedRoot)