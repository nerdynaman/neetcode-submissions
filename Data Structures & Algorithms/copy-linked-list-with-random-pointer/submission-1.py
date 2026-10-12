"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        hashset = {}
        curr = head
        prev = None
        while curr:
            hashset[curr] = Node(curr.val)
            if prev:
                prev.next = hashset[curr]
            prev = hashset[curr]
            curr = curr.next
        
        for i in hashset:
            hashset[i].random = hashset[i.random] if i.random else None
        
        return hashset[head] if head else None