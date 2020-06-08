# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p1, p2 = headA, headB
        flag = 0
        if p1 is None or p2 is None:
            return None
        while p1 != p2:
            if p1.next is not None:
                p1 = p1.next
            else:
                p1 = headB
                flag += 1
            if p2.next is not None:
                p2 = p2.next
            else:
                p2 = headA
                flag += 1
            if flag > 2:
                return None
        return p1