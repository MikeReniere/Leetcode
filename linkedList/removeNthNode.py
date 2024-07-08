from typing import Optional

class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #  2 pointers, one slow, one fast
        dummy = ListNode(0, head) # creates a dummy node to point to the list
        left = dummy
        right = head

        for i in range(0,n):
            right = right.next
            i+= 1

        # shifting the pointers
        while right:
            left = left.next
            right = right.next

        # fast reached the None after the linked list  
        # so slow equals the Nth node 
        # remove the Nth node
        left.next = left.next.next  

        return dummy.next

           
        

    

solution = Solution()
linkedList = ListNode(0, ListNode(2,ListNode(3,ListNode(4,ListNode(5,None)))))
res = solution.removeNthFromEnd(linkedList, 2)

while res:
    print(res.val)
    res = res.next