# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        c1, c2 = l1, l2
        multiplier = 1
        num1 = 0
        num2 = 0

        while c1:
            num1 += multiplier*c1.val
            c1 = c1.next
            multiplier *= 10
        multiplier = 1
        while c2:
            num2 += multiplier*c2.val
            c2 = c2.next
            multiplier*=10
        
        res = num1+num2

        newHead = ListNode(res%10)
        currHead = newHead
        res = res//10
        while res:
            temp = ListNode(res%10)
            currHead.next = temp
            currHead = currHead.next
            res = res//10

        # print()
        return newHead