# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        
        if not root:
            return 

        q   = deque()

        max_sum = float('-inf')
        level = 1
        ans = 1
        q.append(root)

        while q:
            sum = 0

            for _ in range(len(q)):

                temp = q.popleft()
                sum += temp.val

                if temp.left != None:
                    q.append(temp.left)
                if temp.right != None:
                    q.append(temp.right)
                
            if sum > max_sum:
                max_sum = sum 
                ans = level
            level += 1
                
        
        return ans 