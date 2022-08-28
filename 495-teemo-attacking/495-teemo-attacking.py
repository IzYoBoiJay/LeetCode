class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        
        #Base Case: Teemo doesn't attack, that is, there are no timeSeries that he does
        if len(timeSeries) == 0:
            
            return 0
        
        secondsPoisoned = 0
        
        #From 0 to n - 1
        for i in range(0, len(timeSeries) - 1):
        
            secondsPoisoned += min(timeSeries[i + 1] - timeSeries[i], duration)
            
        #To account for timeSeries[n] add duration
        return secondsPoisoned + duration