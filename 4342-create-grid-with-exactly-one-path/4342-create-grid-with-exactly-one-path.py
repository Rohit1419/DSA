class Solution:
    def createGrid(self, m: int, n: int) -> list[str]:
        
        res = [["#"] * n for _ in range(m)]

        for j in range(n):
            res[0][j] = "." 
        
        for i in range(1,m):
            res[i][n-1] = "."

        
        return ["".join(row) for row in res]; 
