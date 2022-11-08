class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        #Base case 1: s and t are length 1 and 
        if len(s) == 1 and len(t) == 1:
            
            return (s == t)
        
        #Base case 2: s and t are not the same length
        if len(s) != len(t):
            
            return False
        
        hashMap = {}
        
        for letter in s:
            
            if letter in hashMap.keys():
                
                hashMap[letter] += 1
                
            else:
                
                hashMap[letter] = 1
                
        for letter in t:
            
            if letter in hashMap.keys():
                
                hashMap[letter] -= 1
                
                if hashMap[letter] < 0:
                    
                    return False
                
            else:
                
                return False
            
            
        return True