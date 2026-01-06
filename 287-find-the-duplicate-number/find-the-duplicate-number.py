class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        slow = 0
        fast = 0

# making sure teh cycle is exists 
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break


# Resent any one pointer to 0 and other the same at braking point
        slow = 0
        
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]
        
        return slow 




        
        

