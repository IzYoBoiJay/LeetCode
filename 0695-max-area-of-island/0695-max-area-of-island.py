class Solution:
    
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        #Nested function to find the area through DFS
        def areaDFS(row, col):
            
            #Check if in bounds, and havent seen yet, and if it is land (base case)
            if row >= 0 and col >= 0 and row < len(grid) and col < len(grid[0]) and (row, col) not in landSeen and grid[row][col] == 1:
                
                #Mark as seen
                landSeen.add((row, col))
                
                #Add 1 and explore
                return(
                    
                    1 +
                    areaDFS(row - 1, col) +
                    areaDFS(row + 1, col) +
                    areaDFS(row, col - 1) +
                    areaDFS(row, col + 1)
                )
            
            else:
                
                #Otherwise add nothing
                return 0
                
        #Tracker variables
        landSeen = set()
        maxArea = 0
        
        #Iterate through grid
        for row in range(len(grid)):
            
            for col in range(len(grid[0])):
                
                #If land found
                if grid[row][col] == 1:
                    
                    #Compare and save the max area
                    maxArea = max(maxArea, areaDFS(row, col))
                    
        #Return the maxArea
        return maxArea