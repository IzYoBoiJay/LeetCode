class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        #Base case: An array of size 1's sum is trivially itself
        if len(nums) == 1:
            
            return nums[0]
        
        #Keep track of the best sum found
        bestSum = nums[0]
        
        #Calculate the current sum per array
        currSum = bestSum
        
        #From Index 1 to n
        for i in range(1, len(nums)):
            
            #If it is negative, reset the current sum
            if currSum < 0:
                
                currSum = 0
                
            #Calculate the sum
            currSum += nums[i]
            
            #If current sum is better, make it the new bestSum, otherwise keep the same
            bestSum = max(bestSum, currSum)
            
        #Return result
        return bestSum
            