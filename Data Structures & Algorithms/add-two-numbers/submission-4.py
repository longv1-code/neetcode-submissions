# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        s1 = []
        s2 = []

        curr = l1
        while curr:
            s1.append(curr.val)
            curr = curr.next

        curr = l2
        while curr:
            s2.append(curr.val)
            curr = curr.next
        
        d1 = 0
        d2 = 0
        while s1:
            length = len(s1) - 1
            d1 += s1.pop() * 10**length
        
        while s2:
            length = len(s2) - 1
            d2 += s2.pop() * 10**length

        total = d1 + d2

        dummy = ListNode(0)
        curr = dummy
        while total != 0:
            digit = total % 10
            curr.next = ListNode(digit)
            curr = curr.next
            total = total // 10
        
        return dummy.next if dummy.next else dummy