# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        carry = 0
        dummy = ListNode(0)
        current = dummy

        while l1 or l2 or carry:

            sum = 0

            if l1:
                val1 = l1.val
            else:
                val1 = 0

            if l2:
                val2 = l2.val
            else:
                val2 = 0

            sum = val1 + val2 + carry
            result = sum%10
            carry = sum//10

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
                

            current.next = ListNode(result)
            current = current.next


                

        
        return dummy.next
