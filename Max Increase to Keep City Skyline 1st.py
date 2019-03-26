

class Solution(object):
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        output1=0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                output1 +=grid[i][j]
                
        gridnew=grid
        
        for i in range(len(grid)):
            a=max(grid[i])
            for j in range(len(grid[i])):
                m=0
                max_col_j=grid[0][j]
                for m in range(len(grid)):
                    if grid[m][j]>max_col_j:
                        max_col_j=grid[m][j]
                gridnew[i][j]=min(a,max_col_j)
        
        output2=0
        for i in range(len(gridnew)):
            for j in range(len(gridnew[i])):
                output2 +=gridnew[i][j]
        
        return output2-output1
