# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        stack = []

        tempHead = head
        count = 0
        while tempHead:
            stack.append(tempHead)
            tempHead = tempHead.next
            count += 1 

        print(stack)

        tempHead = head
        for i in range(count//2):
            temp = stack.pop()
            temp.next = tempHead.next
            tempHead.next = temp
            tempHead = tempHead.next.next
        if tempHead:
            tempHead.next = None
        
