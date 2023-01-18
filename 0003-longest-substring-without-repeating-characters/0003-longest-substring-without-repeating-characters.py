class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        #Hashmap to keep track of the letters seen
        lettersSeen = {}
        
        #Two Pointer approach:
        leftPtr = 0
        rightPtr = 0
        
        #To keep track of the longest substring's length
        longestSSLen = 0
        
        while rightPtr < len(s):
            
            #If the letter has not been seen yet
            if s[rightPtr] not in lettersSeen:
                
                #Mark seen
                lettersSeen[s[rightPtr]] = 1
                
            else:
                
                #Otherwise increment the times seen to the letter mapped
                lettersSeen[s[rightPtr]] += 1
                
            
            #Move the left pointer for to traverse to the end of the substring with repeating chars
            while s[rightPtr] in lettersSeen and lettersSeen[s[rightPtr]] > 1:
                
                #Decrement frequency on what has been seen previously by the right pointer
                lettersSeen[s[leftPtr]] -= 1
                
                #Move left pointer
                leftPtr += 1
                
            #Calculate the current substring length, add 1 for index 0 or case where both pointers are on the same letter
            currSSLen = rightPtr - leftPtr + 1
            
            #If the current substring is longer than the previous longest
            if currSSLen > longestSSLen:
                
                #Update the longest subs
                longestSSLen = currSSLen
                
            #Traverse the right pointer by incrementing it
            rightPtr += 1
                
        #Return the longest substring length
        return longestSSLen