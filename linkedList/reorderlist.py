from typing import Optional
class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # find the middle point
        slow, fast = head, head.next

        while fast != None and fast.next:
            slow = slow.next # shift slow by 1
            fast = fast.next.next # shift fast by 2 
        
        # split the initial list into 2 seperate lists
        second = slow.next 
        slow.next = None 
        prev =  None
        # reverse the 2nd half of the list 
        while second != None:
            temp = second.next
            second.next = prev
            prev = second
            second = temp

        # merge 2 halves lists
        first, second = head,prev # this is because previous is pointing to "4" after reversing the second list

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            # move the pointers
            first = tmp1
            second = tmp2
        while head:
            print(head.val)
            head = head.next

    
solution = Solution()
linkedList = ListNode(1 , ListNode(2,ListNode(3,ListNode(4,None))))
solution.reorderList(linkedList)
