class BrowserHistory:
    
    #Time complexity: O(n) as you have to traverse through the size of the stacks with O(1) pop and push operations
    #Space Complexity: O(n) as there are two one-dimensional stacks

    def __init__(self, homepage: str):
        
        #Taking advantage of the FILO properties, in combo O(n + n) = O(n) space complexity
        self.history = []
        self.ahead = []
        
        #The top of the stack is basically the current page.
        #Just open up a page on a real browser and go to your history!
        self.history.append(homepage)

    def visit(self, url: str) -> None:
        
        #Add to top of the history stack
        self.history.append(url)
        
        #Reset the ahead history
        self.ahead = []

    def back(self, steps: int) -> str:
        
        #While the history stack is NOT empty and we have steps. It must also be assumed that there must always be one element in history, that is current.
        while len(self.history) > 1 and steps > 0:
            
            #Pop the current (top of the history stack) and add it to the ahead stack
            self.ahead.append(self.history.pop())
            
            #Decrement steps
            steps -= 1
            
        #Return the current, aka the top of the history stack
        return self.history[-1]
    
    def forward(self, steps: int) -> str:
        
        #While the stack is NOT empty and we 
        while len(self.ahead) > 0 and steps > 0:
            
            #Pop the latest ahead element (top of the ahead stack) and add it back to the history
            self.history.append(self.ahead.pop())
            
            #Decrement steps
            steps -= 1
            
        #Return the current, aka the top of the history stack
        return self.history[-1]
        
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)