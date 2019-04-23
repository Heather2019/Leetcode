class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        
        lx=len(board)
        ly = len(board[0])
        
        q = list()
        
        for i in range(lx):
            for j in range(ly):
                if board[i][j] == word[0]:
                    q.append((i,j))
        
        def neighbours(board,x,y):
            res=[]
            ds = [(-1,0),(1,0),(0,-1),(0,1)]
            for d in ds:
                xnew = x+d[0]
                ynew = y+d[1]
                if 0<=xnew<lx and 0<=ynew<ly:
                    res.append((xnew,ynew))
            return res
        
        for i in range(len(q)):
            stack = [[q[i][0],q[i][1],0,False]]
            visited = set()
            
            while stack:
                nx,ny,j,dec = stack.pop()
                if dec:
                    visited.remove((nx,ny))
                    continue
                
                visited.add((nx,ny))
                stack.append([nx,ny,j,True])
                
                if j==(len(word)-1):
                    return True
                
                ns = neighbours(board,nx,ny)
                
                for k in range(len(ns)):
                    if ns[k] in visited:
                        continue
                    if board[ns[k][0]][ns[k][1]]==word[j+1]:
                        stack.append([ns[k][0],ns[k][1],j+1,False])
        
        return False
                        
                
