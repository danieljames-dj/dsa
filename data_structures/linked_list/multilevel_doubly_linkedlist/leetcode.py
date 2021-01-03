"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    
    def traverse(self, start):
        while True:
            if start.child != None:
                next = start.next
                start.next = start.child
                start.child = None
                start.next.prev = start
                start = self.traverse(start.next)
                start.next = next
                if next != None:
                    start.next.prev = start
            if start.next is None:
                break
            start = start.next
        return start
    
    def flatten(self, head: 'Node') -> 'Node':
        if head is not None:
            self.traverse(head)
        return head