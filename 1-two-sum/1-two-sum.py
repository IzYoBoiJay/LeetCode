class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        #Base case
        if len(nums) == 0:
            
            return []
        
        
        hashTable = {}
        
        for i in range(len(nums)):
            
            if target - nums[i] in hashTable:
                
                return (hashTable[target - nums[i]] , i)
            
            else:
                
                hashTable[nums[i]] = i