# https://leetcode.com/problems/check-if-there-is-a-valid-path-in-a-grid/description/
class UnionFind: 
    def __init__(self,size): 
        self.f=list(range(size)) 
        
    def find(self,x): 
        if(x==self.f[x]): 
            return x 
        self.f[x ]=self.find(self.f[x]) 
        return self.f[x] 
    
    def union(self,x,y): 
        self.f[self.find(x)]=self.find(y) 
    
class Solution : 
    def getId(self,x,y): 
        return x*self.n+y 
    
    def detectL(self,uf,grid,x,y): 
        if(y-1>=0 and grid[x][y-1 ] in [1,4,6]): 
            uf.union(self.getId(x,y),self.getId(x,y-1)) 
    
    def detectR(self,uf,grid,x,y): 
        if (y+1<len(grid[0]) and grid[x][y+1] in [1,3,5]):
            uf.union(self.getId(x,y),self.getId(x,y+1)) 
            
    def detectD(self,uf,grid,x,y): 
        if(x+1<len(grid) and grid [x+1][y] in [2,5,6]): 
            uf.union(self.getId(x,y),self.getId(x+1,y)) 
    
    def detectU(self,uf,grid ,x,y): 
        if(x-1>=0 and grid[x-1][y] in [2,3,4]): 
            uf.union(self.getId(x,y),self.getId (x-1,y)) 
    
        
    def hasValidPath(self, grid: List[List[int]]) -> bool: 
        m=len(grid) 
        n=len(grid[0]) 
        uf=UnionFind(m*n) 
        self.n=n 
        for i in range(m): 
            for j in range(n): 
                if(grid[i][j]==1): 
                    self.detectL(uf,grid,i,j)
                    self.detectR(uf,grid,i,j) 
                elif(grid[i][j]==2): 
                    self.detectU(uf,grid,i,j) 
                    self.detectD(uf,grid,i,j) 
                elif(grid[i][j]==3): 
                    self.detectL(uf,grid,i,j) 
                    self.detectD(uf,grid,i,j) 
                elif(grid[i][j]==4 ): 
                    self.detectR(uf,grid,i,j) 
                    self.detectD(uf,grid,i,j) 
                elif(grid[i][j]==5): 
                    self.detectL(uf,grid,i, j) 
                    self.detectU(uf,grid,i,j) 
                elif(grid[i][j]==6): 
                    self.detectR(uf,grid,i,j)
                    self.detectU(uf,grid,i,j) 
                    
        return uf.find(self.getId(0,0))==uf.find(self.getId(m-1,n-1))
