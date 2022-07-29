class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        
        #Thinking on the question, I would simply square each element and then call
        #Python's sort() function, but that would make the time complexity O(nlogn)
        #Here is the attempt to make it O(n)
        
        #A data structure I would use is a deque, as one can take advantage of O(1)
        #Insertion AND Access time complexity, however since squaring negatives are
        #always positive, this solution might not work in all cases, especially
        #when comparing what is at the beginning (smallest) of the deque and what is
        #the end of the deque (largest)
        
        #Instead a Two-Pointer approach shall be taken here:

        #As this is not in-place, this brings about O(n) space complexity
        sortedSquares = []
        
        #Left pointer at the beginning index
        leftPtr = 0
        
        #Right pointer at the end index
        rightPtr = len(nums) - 1
        
        #While the left pointer is less than or equal to the right pointer
        while(leftPtr <= rightPtr):
            
            #If the leftPtr squared elem is greater than the rightPtr squared elem
            if nums[leftPtr] ** 2 > nums[rightPtr] ** 2:
                
                #Append it to the new list
                sortedSquares.append(nums[leftPtr] ** 2)
                
                #Increment the left pointer to the right
                leftPtr += 1
                
            #If it leftPtr squared elem is less than the rightPtr squared elem
            else:
                
                #Append it to the new list
                sortedSquares.append(nums[rightPtr] ** 2)
                
                #Decrement the right pointer to the left
                rightPtr -= 1
                
        #Reverse the list as it will be in descending order
        sortedSquares = sortedSquares[::-1]
        
        #Return the new list of sorted squares, O(n) total time complexity
        return sortedSquares