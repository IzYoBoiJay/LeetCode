class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        lowest = float('inf')
        
        potentialProfit = 0
        profit = 0
        
        for priceToday in prices:
            
            if priceToday < lowest:
                
                lowest = priceToday
                
            potentialProfit = priceToday - lowest
            
            if potentialProfit > profit:
                
                profit = potentialProfit
                
        return profit