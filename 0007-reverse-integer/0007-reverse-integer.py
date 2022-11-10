class Solution:
    def reverse(self, x: int) -> int:
        
        minInt = int(-math.pow(2, 31))
        maxInt = int(math.pow(2, 31) -1)

        xStr = str(x)
        
        xStr = xStr[::-1]
        
        if xStr[len(xStr) - 1] == '-':
            
            xStr = xStr[:-1]
            xStr = '-' + xStr
            
        reversedX = int(xStr)
        
        if reversedX < minInt or reversedX > maxInt:
            
            return 0
        
        else:
            
            return reversedX
            
        