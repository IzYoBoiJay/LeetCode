# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        #Base case: Empty
        if head is None:
            
            return None
        
        #Base case 2: Singular Node
        if head.next is None:
            
            return head
        
        turtle = head
        hare = head
        
        while turtle is not None or hare is not None:
            
            #Turtle moves 1
            turtle = turtle.next
            
            #Hare moves 2
            hare = hare.next.next
            
            if hare is None or hare.next is None:
                
                break
                
        return turtle