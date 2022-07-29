class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        #O(n) Time Complexity and O(1) Space Complexity as it is In-Place
        
        #Counter variable to keep track
        evenDigitsCount = 0
        
        #Iterate through the nums array
        for i in range(len(nums)):
            
            #If the length of the element as a string is even
            if len(str(nums[i])) % 2 == 0:
                
                #Increment
                evenDigitsCount += 1
        
        #Return the count
        return evenDigitsCount