# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def maxProduct(self, root: Optional[TreeNode]) -> int:
        self.max_product = float('-inf')
        mod = 10 ** 9 + 7 

        self.total_sum = self.find_sum(root)

        self.find_product(root)
       
        return self.max_product % mod


    def find_sum(self, root):
        if not root:
            return 0
        
        return self.find_sum(root.left) + root.val + self.find_sum(root.right)

    def find_product(self, root):
        if not root:
            return 0
        
        left_sum = self.find_product(root.left)

        right_sum = self.find_product(root.right)

        subtree_sum = left_sum  + right_sum + root.val 

        product = (self.total_sum - subtree_sum) * subtree_sum
        self.max_product = max(self.max_product, product)

        return subtree_sum



        




        
