class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        
        #Create an empty list
        selfDivNums = []
        
        #Iterate through range of numbers
        #For loop works from n to m - 1, we add 1 to ensure range [n, m]
        for num in range(left, right + 1):
            
            #Consider the number is already self-dividing
            selfDivNums.append(num)
            
            #Evaluate the num's digits
            for digitChar in str(num):
                
                digit = int(digitChar)
                
                #If the modulo of the int cast of the digit char is NOT 0, it is not divisible. Neither is anything mod by 0.
                if digit == 0 or num % digit != 0:
                    
                    #Remove from the list, if the element is there and break the loop to prevent further popping
                    if len(selfDivNums) > 0:
                        
                        selfDivNums.pop()
                        break                        
        
        return selfDivNums
    
        #Time complexity: O(n x m) where n is the range of numbers, and m is the digits of the numbers
        #Space complexity: O(n) for the 1-Dimensional list