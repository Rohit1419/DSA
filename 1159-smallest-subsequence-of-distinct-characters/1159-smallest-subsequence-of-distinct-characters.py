class Solution:
    def smallestSubsequence(self, s: str) -> str:
        
        n = len(s)
        index = {}

        for i , ch in enumerate(s):
            index[ch] = i 
        

        stack = []
        visited = set()

        for i, ch in enumerate(s):

            if ch in visited:
                continue 
            
            while stack and stack[-1] > ch and index[stack[-1]] > i :

                visited.remove(stack.pop())
            
            visited.add(ch)
            stack.append(ch)
        
        return "".join(stack)



        
           
            
