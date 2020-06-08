# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        sum = l1.val + l2.val
        dummyHead = ListNode(0)
        carry = 0
        node = dummyHead
        while l1 is not None or l2 is not None or carry > 0:
            sum = carry
            if l1 is not None:
                sum += l1.val
                l1 = l1.next
            if l2 is not None:
                sum += l2.val
                l2 = l2.next
            node.next = ListNode(sum % 10)
            carry = sum // 10
            node = node.next
        return dummyHead.next