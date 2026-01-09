# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        
        def postorder(node):
            if not node:
                return (None, 0)
            
            left_node, left_hight = postorder(node.left)
            right_node, right_hight = postorder(node.right)

            if left_hight > right_hight:
                return left_node, left_hight + 1
            
            elif left_hight < right_hight:
                return right_node, right_hight + 1
            
            return node, left_hight + 1    # if hight are equal then curruent node is LCA

        
        node, _ = postorder(root)
        return node