class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        # we aso have another stack based method -- so check in submissions
        depth , score = 0 , 0

        for i, ch in enumerate(s): 

            if ch == '(' :
                depth += 1
            
            else: 
                depth -= 1
                if s[i -1] == '(':
                    score += 1 <<(depth) # this leftshift is equallent to 2 ^ depth

        return score