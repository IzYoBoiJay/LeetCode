# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        
        #Base cases: Empty or Singular Node trivially has no cycle:
        if head is None or head.next is None:
            return False
        
        #Turtle and Hare -> O(1) Space Complexity!
        turtle = head
        hare = head
        
        while turtle is not None or hare is not None:
            
            turtle = turtle.next
            
            hare = hare.next.next
            
            if hare is None or hare.next is None:
                
                break
                
            if turtle == hare:
                
                return True
            
        return False