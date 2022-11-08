class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        #Base case
        if len(s) == 1:
            
            return True
        
        formattedStr = ''
        
        for c in s:
            
            #If the char is alpha
            if c.isalpha():
                
                #Append lowercase version as formatted string
                formattedStr += c.lower()
                
            #If the char is numeric
            elif c.isdigit():
                
                #Append digit
                formattedStr += c
                
            else:
                
                continue
                
        #Return the result of the comparison of the reverse to original
        return formattedStr[::-1] == formattedStr