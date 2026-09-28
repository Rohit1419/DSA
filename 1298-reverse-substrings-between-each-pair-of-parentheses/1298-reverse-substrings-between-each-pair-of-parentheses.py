class Solution:
    def reverseParentheses(self, s: str) -> str:
        
        stack = [[]]

        for c in s : 
            if c == '(':
                stack.append([])
            elif c == ')':
                pop = stack.pop()
                stack[-1].extend(reversed(pop))
            else:
                stack[-1].append(c)
        
        return "".join(stack[0])
    
        