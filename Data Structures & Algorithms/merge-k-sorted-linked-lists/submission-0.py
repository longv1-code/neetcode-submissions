# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()   
        for i in range(len(lists)):
            head = lists[i] # head pointer to current linkedlist
            curr = dummy

            while head:
                if curr.next == None or head.val < curr.next.val:
                    nxt = curr.next
                    curr.next = ListNode(head.val, nxt)
                    head = head.next
                curr = curr.next
        
        return dummy.next