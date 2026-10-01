class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        
        # Recursively reverse the rest of the list
        new_head = self.reverseList(head.next)
        
        # Fix the current connection
        front = head.next          
        front.next = head          
        head.next = None          
        
        return new_head  # Return the head of the reversed list
        
