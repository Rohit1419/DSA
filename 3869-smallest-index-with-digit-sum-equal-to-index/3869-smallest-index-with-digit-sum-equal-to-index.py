class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        

        n = len(nums)

        # min_index = 0 

        def findsum(num):
            sum = 0
            while num > 0:
                digit = num % 10 ; 
              
                sum = sum + digit 
                num = num // 10 
        

            return sum 
        
        for i in range(n):

            if i == findsum(nums[i]):
                return i 
        
        return -1 

            
        
