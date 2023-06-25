class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        
        #Assumption: sr and sc aka the starting row and columns are always valid (in bounds)
        
        rows = len(image)
        columns = len(image[0])
        
        #Base case: Starting pixel is already the color
        if image[sr][sc] == color:
            
            #Make no changes
            return image
        
        startingColor = image[sr][sc]
        
        #Depth-First Search
        def dfs(x, y):
            
            #If the pixel is starting color
            if image[x][y] == startingColor:
            
                #Apply change
                image[x][y] = color

                #Left
                if (x - 1) >= 0:

                    dfs(x - 1, y)

                #Right
                if (x + 1) < rows:

                    dfs(x + 1, y)

                #Up
                if (y - 1) >= 0:

                    dfs(x, y - 1)

                #Down
                if (y + 1) < columns:

                    dfs(x, y + 1)
                
        #Call DFS with the starting row and column
        dfs(sr, sc)
        
        #Return the modified image
        return image