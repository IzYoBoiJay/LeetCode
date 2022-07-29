class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        
        #To construct a ransom note, one must have the letters AND
        #the amount of that letter from a magazine. To achieve a O(n)
        #time complexity we take advantage of hashmap average O(1) insertion and
        #look up time at the cost of O(n) space complexity
        
        lettersAvailable = {}
        canConstruct = True
        
        for letter in magazine:
            
            if letter in lettersAvailable:
                
                lettersAvailable[letter] += 1
                
            else:
                
                lettersAvailable[letter] = 1
                
        for letter in ransomNote:
            
            if letter in lettersAvailable and lettersAvailable[letter] > 0:
                
                lettersAvailable[letter] -= 1
                
            else:
                
                canConstruct = False
                
        return canConstruct
                