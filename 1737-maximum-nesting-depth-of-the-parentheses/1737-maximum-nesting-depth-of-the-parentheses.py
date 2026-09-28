class Solution:
    def maxDepth(self, s: str) -> int:
        max_cnt = 0 
        curr_cnt = 0 

        for ch in s : 
            if ch == '(':
                curr_cnt += 1
                max_cnt = max(max_cnt, curr_cnt)
            
            elif ch == ')':
                curr_cnt -= 1

            
        
        return max_cnt
