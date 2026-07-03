class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        
        window  = defaultdict(int)
        window_sum  = 0
        max_sum = 0
        
        max_sum = window_sum

        l = 0
        
        for r in range(len(nums)):
            
            window_sum += nums[r]
            window[nums[r]] += 1 

            if r - l + 1 > k:
                window[nums[l]] -= 1
                if  window[nums[l]] == 0:
                    window.pop(nums[l])
                window_sum -= nums[l]
                
                l+= 1
            
            if len(window) == k and r - l + 1 == k:

                max_sum = max(max_sum, window_sum)

        
        return max_sum