class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:


        def check_lenght(node):
            if node == None:
                return False
            for _ in range(k-1):
                node = node.next
                if node == None:
                    return False
            return True


        def get_k_values(node):
            dummy = node
            values = [node.val]
            for _ in range(k-1):
                dummy = dummy.next
                values.append(dummy.val)

            return values
        
        def set_k_values(values, node):
            for i in range(k-1,-1,-1):
                node.val = values[i]
                node = node.next

        def get_next_start(node):
            next_start = node
            for _ in range(k):
                next_start = next_start.next
            return next_start

        node = head

        while check_lenght(node):
            values = get_k_values(node)
            set_k_values(values, node)
            node = get_next_start(node)
        return head
