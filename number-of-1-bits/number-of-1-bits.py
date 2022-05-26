class Solution:
    def hammingWeight(self, n: int) -> int:
        
        oneBits = 0
        
        #Format as binary string
        binaryStr = format(n, 'b')
        
        #Iterate through binary string
        for bit in binaryStr:
            
            #If the bit is found to be 1
            if bit == '1':
                
                #Increment count
                oneBits += 1    
                
        #Return count
        return oneBits
    
        #Time Complexity: O(n) where n is the number of bits