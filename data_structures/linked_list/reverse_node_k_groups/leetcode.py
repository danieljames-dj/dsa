# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        dummyHead = ListNode(0)
        dummyHead.next = head
        last = dummyHead
        while True:
            nextLast = last.next
            temp = last.next
            for _ in range(k):
                if temp is None:
                    return dummyHead.next
                temp = temp.next
            cur = last.next
            curNext = cur.next
            for _ in range(k-1):
                tempCur = curNext.next
                curNext.next = cur
                cur = curNext
                curNext = tempCur
            last.next = cur
            nextLast.next = curNext
            last = nextLast
        return None