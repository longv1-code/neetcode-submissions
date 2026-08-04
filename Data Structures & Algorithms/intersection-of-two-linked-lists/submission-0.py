# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        while headA:
            curr = headB
            while curr:
                if headA == curr:
                    return headA
                curr = curr.next
            headA = headA.next
        
        return None