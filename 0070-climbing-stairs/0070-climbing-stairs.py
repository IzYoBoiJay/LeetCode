class Solution:
    
    def climb(self, n, cache):
        
        #If stairs already climbed before
        if n in cache:
            
            return cache[n]
        
        #Otherwise, climb stairs
        else:
            
            cache[n] = self.climb(n - 1, cache) + self.climb(n - 2, cache)
            
            return cache[n]
        

    def climbStairs(self, n: int) -> int:
        
        #It's Finonacci! We can memoize it to make it more efficient.
        
        #Base cases:
        if n <= 0:
            
            return 0
        
        elif n == 1:
            
            return 1
        
        elif n == 2:
            
            return 2
            
        else:
            
            #Utilize a hash table as a cache
            cache = {}
            
            #Setup the cache
            cache[0] = 0
            cache[1] = 1
            cache[2] = 2
            
            return self.climb(n, cache)