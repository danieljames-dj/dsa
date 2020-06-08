# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        cur = dummyHead
        while cur.next is not None and cur.next.next is not None:
            if cur.next.val == cur.next.next.val:
                valToDel = cur.next.val
                while cur.next is not None and cur.next.val == valToDel:
                    nodeToDel = cur.next
                    cur.next = cur.next.next
                    del nodeToDel
            else:
                cur = cur.next
        return dummyHead.next