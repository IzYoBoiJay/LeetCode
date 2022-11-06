class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        
        #Base case: If the size is 1 or less, than there can be no duplicates
        if len(nums) <= 1:
            
            return False
        
        #Brute force: Do a nested for loop to scan for duplicate of the current element, but this is O(n^2). If there is more space, we can optimize it
        #Hash map: If it is not found yet, make it a key. If the key exists, return False. This takes advantage of O(1) lookup time of a map, and optimizes to O(n)
        
        found = {}
        
        for i in range(len(nums)):
            
            #If key exists in the found hash map
            if nums[i] in found:
                
                return True
            
            else:
                
                found[nums[i]] = True #some sentinel value
                
        #If no duplicate was found, the for loop will end, and result to False by default
        return False