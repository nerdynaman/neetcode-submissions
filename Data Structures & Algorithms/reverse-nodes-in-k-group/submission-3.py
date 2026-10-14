# Definition for singly-linked list.

# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        curr = head
        count = 0
        while curr:
            count += 1
            curr = curr.next

        ranges = count // k 

        currHead = head
        prev = None

        # tails = [0 for i in range(ranges)]
        # heads = [0 for i in range(ranges)]
        resultHead = None
        groupTail = None

        for i in range(ranges):
            localCounter = 0
            head = currHead
            while localCounter < k:
                temp = currHead.next
                currHead.next = prev
                prev = currHead
                currHead = temp
                localCounter += 1
            
            if not resultHead:
                resultHead = prev
            if groupTail:
                groupTail.next = prev
            groupTail = head
            prev = None

        if currHead:
            groupTail.next = currHead
            
        return resultHead