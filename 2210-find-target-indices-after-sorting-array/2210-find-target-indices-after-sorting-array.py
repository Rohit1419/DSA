class Solution:
    def targetIndices(self, nums: list[int], target: int) -> list[int]:
        
        less = 0 
        count = 0 

        for n in nums:
            if n < target: 
                less += 1
            elif n == target: 
                count += 1
        
        return list(range(less, count + less))