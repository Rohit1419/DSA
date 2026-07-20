class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        last_index = {}

        for i, ch in enumerate(s):
            last_index[ch] = i 
        
        stack = []
        visited = set()

        for i, ch in enumerate(s):

            if ch in visited:
                continue
            
            while stack and stack[-1] > ch and last_index[stack[-1]] > i:
                visited.remove(stack.pop())

            
            visited.add(ch)
            stack.append(ch)
        
        return "".join(stack)