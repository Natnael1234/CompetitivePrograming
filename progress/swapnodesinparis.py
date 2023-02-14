# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur, prev = head, None
        while cur and cur.next:
            first, second = cur, cur.next
            if prev:
                prev.next = second
            else:
                head = second
            first.next = second.next
            cur = second
            second.next = first
            prev = first
            if cur.next and cur.next.next:
                cur = cur.next.next
            elif cur.next:
                break
        return head
