# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: ListNode) -> None:
        if head is None or head.next is None:
            return head
        mid, fast = head, head.next
        while fast != None and fast.next != None:
            mid = mid.next
            fast = fast.next.next
        midHead = mid.next
        mid.next = None
        node = midHead.next
        midHead.next = None
        while node != None:
            temp = node.next
            node.next = midHead
            midHead = node
            node = temp
        node1 = head
        node2 = midHead
        while node2 != None:
            temp = node2.next
            node2.next = node1.next
            node1.next = node2
            node2 = temp
            node1 = node1.next.next
        return head