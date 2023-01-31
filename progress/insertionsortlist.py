# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head == None: 
            return head
        res = []
        dummy = head
        while dummy != None:
            res.append(dummy.val)
            dummy = dummy.next
        res.sort()
        dummy = head
        for i in res:
            dummy.val = i
            dummy = dummy.next
        return head
