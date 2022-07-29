class Solution:
    def firstUniqChar(self, s: str) -> int:
        
        index = 0
        
        for char in s:

            if s.count(char) == 1:

                return index
            
            index += 1

        return -1