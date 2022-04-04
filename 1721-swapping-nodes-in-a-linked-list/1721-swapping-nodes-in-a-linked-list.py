# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        tmp1 = head
        for i in range(k-1):
            tmp1 = tmp1.next
            k-=1
        tmp2, tail = head, tmp1
        while tail.next != None:
            tmp2 = tmp2.next
            tail = tail.next
        tmp = tmp2.val
        tmp2.val = tmp1.val
        tmp1.val = tmp
        return head
        