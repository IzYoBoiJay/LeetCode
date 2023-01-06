class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        
        if len(nums) == 1:
            
            return nums[0]
        
        else:
            
            elementFreq = {}
            majorityElement = nums[0]
            
            for i in range(len(nums)):
                
                if nums[i] in elementFreq:
                    
                    elementFreq[nums[i]] += 1
                    
                else:
                    
                    elementFreq[nums[i]] = 1
                    
            
                    
            for element in elementFreq:
                
                if elementFreq[element] > elementFreq[majorityElement]:
                    
                    majorityElement = element
                    
            return majorityElement
                