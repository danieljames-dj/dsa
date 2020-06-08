"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        node = head
        if head is None:
            return None
        while node != None:
            newNode = Node(node.val)
            newNode.next = node.next
            node.next = newNode
            node = newNode.next
        node = head
        while node != None:
            if node.random is None:
                node.next.random = None
            else:
                node.next.random = node.random.next
            node = node.next.next
        node = head
        newHead = head.next
        newNode = newHead
        while node != None:
            node.next = node.next.next
            node = node.next
            if node is None:
                newNode.next = None
            else:
                newNode.next = node.next
            newNode = newNode.next
        return newHead