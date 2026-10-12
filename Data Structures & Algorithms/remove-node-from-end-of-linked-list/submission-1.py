# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        count = 0
        curr = head
        while curr:
            count += 1
            curr = curr.next
        
        curr = head
        prev = None
        count -= n
        while count != 0:
            prev = curr
            curr = curr.next
            count -= 1

        if prev:
            prev.next = curr.next
        else:
            return head.next
        
        return head