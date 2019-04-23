class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        if not grid:
            return 0
        
        m = len(grid)
        n = len(grid[0])
        res=0
        
        def _island(grid,i,j):
            stack = [[i,j]]
            while stack:
                x,y = stack.pop()
                if grid[x][y] == '0':
                    continue
                
                grid[x][y] = '0'
                
                ds = [(-1,0),(1,0),(0,-1),(0,1)]
                
                for d in ds:
                    if 0<=x+d[0]<m and  0<=y+d[1]<n:
                        stack.append([x+d[0],y+d[1]])
                        
                
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    res = res +1
                    _island(grid,i,j)
        
        return res
