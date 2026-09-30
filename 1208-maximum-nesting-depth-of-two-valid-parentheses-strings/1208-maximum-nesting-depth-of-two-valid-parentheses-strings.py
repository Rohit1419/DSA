class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        
        depth = 0  
        res = [] 

        for c in seq:


            if c =='(':
                depth += 1
                res.append((depth -1) % 2 )
            else:
                depth -=1 
                res.append(depth % 2)

            
        return res 

        