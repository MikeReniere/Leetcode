from typing import Optional

class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        slow, fast = head, head
        # this moves each pointer 1, and 2 spots for the slow and fast pointers
        while fast and fast.next: # want to make sure these are not null, fast and fast.next because fast is moving two
            slow  = slow.next
            fast = fast.next.next
            if slow == fast:
                return True

        return False