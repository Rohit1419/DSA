class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        
        m = len(matrix)
        n = len(matrix[0])

        low = 0
        high = m * n - 1

        while low <= high:
            mid = low + (high - low)//2

            # mid element cordinates
            row = mid // n
            col = mid % n

            if matrix[row][col] == target:
                return True
            
            elif matrix[row][col] > target:
                high -= 1
            else:
                low += 1

        
        return False 
        

