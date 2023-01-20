class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = head
        end = head
        while end and end.next:
            mid = mid.next
            end = end.next.next
        
        return mid
