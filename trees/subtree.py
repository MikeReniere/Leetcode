from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not subRoot: return True # a null subTree is always a subtree of a non null tree
        if not root and subRoot: return False # if subRoot is not null, and root is null, subRoot will never be a subTree of root

        # both trees are not empty

        if self.sameTree(root, subRoot):
            return True
        
        if (self.isSubtree(root.left, subRoot) or self.isSubtree(root.right,subRoot)):
            return True
        else:
            return False

    def sameTree(self, root,subRoot):
        if not root and not subRoot: # if both are empty
            return True    
        
        if root and subRoot and root.val == subRoot.val: # if they are not empty, and the top nodes are the same, recursively check every node in the trees
            return (self.sameTree(root.left,subRoot.left) and 
            self.sameTree(root.right,subRoot.right))

        # if one is empty, and one isnt empty - we get here
        return False # a null tree is always a subtree of a non null tree  -- so this is not the same tree
        
   
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



root2 = TreeNode(2)
root2.left = TreeNode(2, TreeNode(4), TreeNode(5))

isSubTree = solution.isSubtree(root,root2)

print(isSubTree)