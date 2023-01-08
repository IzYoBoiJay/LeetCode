class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        #To keep track of the furthest index able to reach
        maxIndex = 0
        
        #Iterate through each element in nums
        for i, jumpNum in enumerate(nums):
            
            #Reached an index that cannot be reached (further than the maxIndex possible)
            if i > maxIndex:
                
                return False
            
            #Compare the current maxIndex to the current index plus its jump to determine a new maxIndex
            maxIndex = max(maxIndex, i + jumpNum)

        #Able to reach the end as the condition where the maxIndex and the last index is the same
        return True
            