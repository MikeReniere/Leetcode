from typing import Optional

class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        tail = dummy # tail of the outputList

        while list1 and list2: # iterate through both lists while both lists have values in them
            if list1.val < list2.val:
                tail.next = list1 
                list1 = list1.next # updates the list1 "pointer" to the next node in list1
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next

        # if either of thse 
        if list1: 
            tail.next = list1
        elif list2:
            tail.next = list2 

        return dummy.next   


solution = Solution()
linkedList1 = ListNode(1, ListNode(2,ListNode(4,None)))
linkedList2 = ListNode(1, ListNode(3,ListNode(4,None)))
res = solution.mergeTwoLists(linkedList1,linkedList2)


while res:
    print(res.val)
    res = res.next
