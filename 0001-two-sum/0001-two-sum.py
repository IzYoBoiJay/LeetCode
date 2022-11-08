class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Base Case
        if len(nums) == 2:
            
            return [0, 1]
        
        #a + b = c
        #c - b = a
        
        hMap = {}
        
        
        for i in range(len(nums)):
            
            if nums[i] in hMap:
                
                return [hMap[nums[i]], i]
            
            else:
                
                hMap[target - nums[i]] = i