class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        
        #Base Case
        if len(word1) == 3 and len(word2) == 3:
            
            return True
        
        hMap = {}
        
        for c in word1:
            
            if c in hMap:
                
                hMap[c] += 1
                
            else:
                
                hMap[c] = 1
                
        for c in word2:
            
            if c in hMap:
                
                hMap[c] -= 1
                
            else:
                
                hMap[c] = -1
                
        for c in hMap:
            
            if abs(hMap[c]) > 3:
                
                return False
            
        return True