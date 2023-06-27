class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        
        #Base Case: Any string with a single char is trivially a palindrome, which means it is arbitrarily in the middle.
        if len(palindrome) == 1:
            
            return ''
        
        #For something to be lexographically small (that I googled, must be the from the earliest letter of alphabet aka a)
        #But what about strings full of a's? Then to keep them in the order such that a -> b just make the last char b
        #As for any other string, the first instance of a letter not being a, just make it an a.
        
        
        #For a Python approach, strings are immutable, so in this case let's convert it into a list
        broken = list(palindrome)
        
        #Create a right pointer to check for the middle
        rightPtr = len(broken) - 1
        
        #For each character in the palindrome string
        for i in range(len(broken)):
            
            #Case where changing the middle basically does nothing, we need to skip it
            #This applies to odd number of chars
            if i == rightPtr:
                
                #Skip
                continue
            
            #If it is not an a, set it to an a
            if broken[i] != 'a':
                
                #Make the change
                broken[i] = 'a'
                
                #Return the result
                return ''.join(broken)
            
            #Decrement the right pointer
            rightPtr -= 1
            
        #If the for loop completes, then the string were all a's, set the last char to a b
        broken[len(broken) - 1] = 'b'
        
        #Return the result
        return ''.join(broken)