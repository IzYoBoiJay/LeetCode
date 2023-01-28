class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        
        #Base case
        if n < 1:
            
            return False
        
        return (pow(3, 19) % n == 0)