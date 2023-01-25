class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        tmp = head
        array = []
        while tmp:
            array.append(tmp.val)
            tmp = tmp.next
          
        array.sort()
        tmp = head
        for num in array:
            tmp.val = num
            tmp = tmp.next
        return head
