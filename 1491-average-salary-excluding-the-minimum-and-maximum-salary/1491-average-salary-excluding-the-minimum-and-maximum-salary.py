class Solution:
    def average(self, salary: List[int]) -> float:
        
        total = 0
        count = 0
        
        low = min(salary)
        high = max(salary)
        
        for i in range(len(salary)):
            
            if salary[i] == low or salary[i] == high:
                
                continue
                
            total += salary[i]
            count +=1
            
        return (total / count)