# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        str1 = ""
        str2 = ""

        while l1 is not None:
            str1 += str(l1.val)
            l1 = l1.next

        while l2 is not None:
            str2 += str(l2.val)
            l2 = l2.next

        str1 = str1[::-1]
        str2 = str2[::-1]

        num1 = int(str1)
        num2 = int(str2)

        sumTwoNums = num1 + num2
        sumStr = str(sumTwoNums)
        sumStr = sumStr[::-1]

        twoNumsList = ListNode()
        head = twoNumsList

        twoNumsList.val = int(sumStr[0])

        for i in range(1, len(sumStr)):

            twoNumsList.next = ListNode(int(sumStr[i]))
            twoNumsList = twoNumsList.next
            
        return head

