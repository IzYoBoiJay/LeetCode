class Solution:
    def isValid(self, s: str) -> bool:
        
        
        #If the length of the string is odd, then there can be no ending char or Length is trivially 1
        if (len(s) % 2 != 0) or (len(s) == 1):
            
            return False
        
        #Lesser known base case: If the string starts with a closer, there is no way it is valid
        if s[0] in ')}]':
            
            return False
        
        #Hashmap for pairs O(n) space
        pairs = {
            '(' : ')',
            '{' : '}',
            '[' : ']'
        }
        
        #Stack to push openers O(n) space
        openers = []

        
        #Iterate through the string
        for i in range(len(s)):
            
            #If current char is an opener
            if s[i] in pairs.keys():
                
                #Push to stack
                openers.append(s[i])
                 
            #Otherwise it is a closer
            else:  
                
                if len(openers) == 0:
                    
                    return False
                
                opener = openers.pop()
                
                #If the latest opener is not a pair for the closer
                if pairs[opener] != s[i]:
                    
                    return False
                
                #If it is then continue
                else:
                    
                    continue
            
        #If stack is empty, then it is valid
        return (len(openers) == 0)
    
        #O(n) time complexity taking advantage of O(1) key search and O(1) push/pop operations and iterates through string once
        #O(n + n) = O(n) space complexity from 1-D stack and 1-D hashmap