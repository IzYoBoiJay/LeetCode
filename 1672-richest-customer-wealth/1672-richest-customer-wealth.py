class Solution:
    
    def calcSum(self, account):
        
        total = 0
        
        for i in range(len(account)):
            
            total += account[i]
            
        return total
        
        
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        maxWealth = 0
        
        for i in range(len(accounts)):
            
            accountTotal = self.calcSum(accounts[i])
            
            if accountTotal > maxWealth:
                
                maxWealth = accountTotal
                
        return maxWealth