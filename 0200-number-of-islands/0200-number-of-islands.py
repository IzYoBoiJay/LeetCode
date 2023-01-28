class Solution:
    
    """
    The thought process I am going to approach here is that a MxN matrix is given
    This by nature is a binary matrix of either '1' or '0'. If DFS is used, there would be a need
    to mark that a '1' has been visited. Since the '0' are being checked against, to save space, one
    can mark the '1' as visited by changing it to a '0'. As the algorithm iterates through the matrix,
    it will do a DFS. As the island is explored, increment a variable tracking it, and continue iterating
    through the matrix to find the next instance of an island. BFS can also be used to solve this problem.
    """
    
    def DFS(self, grid, row, col, totalRows, totalCols):
        
        
        #Mark as "visited" by making it water
        grid[row][col] = '0'

        #Left
        if row - 1 >= 0 and grid[row - 1][col] == '1':

            self.DFS(grid, row - 1, col, totalRows, totalCols)

        #Right
        if row + 1 < totalRows and grid[row + 1][col] == '1':

            self.DFS(grid, row + 1, col, totalRows, totalCols)

        #Down
        if col - 1 >= 0 and grid[row][col - 1] == '1':

            self.DFS(grid, row, col - 1, totalRows, totalCols)

        #Up
        if col + 1 < totalCols and grid[row][col + 1] == '1':

            self.DFS(grid, row, col + 1, totalRows, totalCols)
            
    
    
    def numIslands(self, grid: List[List[str]]) -> int:
        
        #Base case 1: Grid does not exist
        if grid is None:
            
            return 0
    
        #Get the number of rows and columns
        totalRows = len(grid)
        totalCols = len(grid[0])
        
        #Base case 2: The grid is trivially 1x1, and there is an island or not
        if totalRows == 1 and totalCols == 1:
            
            #Return whether it is an island or not
            return int(grid[0][0])
        
        
        #Variable to keep track the number of islands
        islands = 0
        
        #Iterate through the grid
        for row in range(totalRows):
            
            for col in range(totalCols):
                
                #If land is found
                if grid[row][col] == '1':
                    
                    print('islandfound')
                    #Island found
                    islands += 1
                    
                    #DFS
                    self.DFS(grid, row, col, totalRows, totalCols)
                    
        return islands