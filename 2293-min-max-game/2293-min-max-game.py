class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        
        #Base case, the min is found
        if len(nums) == 1:
        
            return nums[0]
        
        else:
            
            newNums = []
            
            #O(logn)
            for i in range(int(len(nums) / 2)):
                
                #Even
                if i % 2 == 0:
                    
                    newNums.append(min(nums[2 * i], nums[2 * i + 1]))
                
                #Odd
                else:
                    
                    newNums.append(max(nums[2 * i], nums[2 * i + 1]))
                    
            #Recursively search
            return self.minMaxGame(newNums)