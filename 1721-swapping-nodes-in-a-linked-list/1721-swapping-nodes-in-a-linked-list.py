# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        tmp1, tmp2 = head, head
        count = 1
        while tmp1.next != None:
            tmp1 = tmp1.next
            count += 1
        tmp1 = head
        for i in range(k-1):
            tmp1 = tmp1.next
        for i in range(count-k):
            tmp2 = tmp2.next
        tmp1.val, tmp2.val = tmp2.val, tmp1.val
        return head
        