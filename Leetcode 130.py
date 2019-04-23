class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        
        if not board:
            return board
        
        m=len(board)
        n=len(board[0])
        
        def _solve(i,j):
            stack = [[i,j]]
            ds = [(0,1),(0,-1),(1,0),(-1,0)]
            
            while stack:
                tem = stack.pop()
                if board[tem[0]][tem[1]]=='X' or board[tem[0]][tem[1]]=='*':
                    continue
                
                board[tem[0]][tem[1]] = '*'
                
                for d in ds:
                    if 0<=(tem[0] + d[0])<m and 0<=(tem[1] + d[1])<n:
                        stack.append([tem[0] + d[0],tem[1] + d[1]])
                        
        for i in range(m):
            list(map(_solve,(i,i),(0,n-1)))
        
        
        for i in range(n):
            list(map(_solve,(0,m-1),(i,i)))       
        
        
        for i in range(m):
            for j in range(n):  
                if board[i][j]=='O':
                    board[i][j]='X'
                if board[i][j]=='*':
                    board[i][j]='O'
                    
        return board
 
