# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        if head is not None and head.next is not None:
            dummyHead = ListNode(0)
            dummyHead.next = head
            last = dummyHead
            while last.next is not None and last.next.next is not None:
                temp = last.next
                last.next = temp.next
                temp.next = last.next.next
                last.next.next = temp
                last = last.next.next
            head = dummyHead.next
        return head