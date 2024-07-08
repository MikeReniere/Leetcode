from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not p and not q: # both of them are null
            return True
        if not p or not q: #only one of them is null
            return False
        if p.val != q.val: # checks the value 
            return False
        # both p and q are non empty, and the values are the same

        return (self.isSameTree(p.left,q.left) and 
        self.isSameTree(p.right,q.right))



        
   
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

root2 = TreeNode(1)
root2.left = TreeNode(2, TreeNode(4), TreeNode(5))
root2.right = TreeNode(3, None, TreeNode(6))

isSame = solution.isSameTree(root,root2)

print(isSame)