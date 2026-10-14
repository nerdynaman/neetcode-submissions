# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 1:
            return lists[0]
        elif not lists:
            return None

        while len(lists) > 1:
            currMerges = []
            for i in range(0, len(lists),2):
                left= lists[i]
                right = None if i+1>=len(lists) else lists[i+1]
                res = self.mergeLists(left, right)
                currMerges.append(res)
            lists = currMerges

        return lists[0]
        
    
    def mergeLists(self, left, right):
        if left == None:
            return right if right != None else None
        if right == None:
            return left if left != None else None

        lCurr, rCurr = left, right
        if lCurr.val <= rCurr.val:
            master = lCurr
            lCurr = lCurr.next
        else:
            master = rCurr
            rCurr = rCurr.next

        curr = master
        while lCurr and rCurr:
            if lCurr.val <= rCurr.val:
                minVal = lCurr
                lCurr = lCurr.next
            else:
                minVal = rCurr
                rCurr = rCurr.next

            curr.next = minVal
            minVal.next = None
            curr = curr.next
        
        curr.next = lCurr if lCurr else rCurr
        return master