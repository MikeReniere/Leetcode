from typing import Optional

class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        # dummy = ListNode(0) # dummy node 
        # curr = dummy
        # carryValue = 0

        # while l1 or l2 or carryValue != 0: # also checks for carry - covers the edge case of 8 + 7 = 15
        #     v1 = l1.val if l1 else 0 #gets values from each node if they are not null 
        #     v2 = l2.val if l2 else 0  # if they are null, sets the value to 0

        #     # compute new digit
        #     val = v1 + v2 + carryValue
        #     carry = val // 10 # gets the carry
        #     val  = val % 10 # gets the one place
        #     curr.next = ListNode(val)

        #     # updating the pointers
        #     curr = curr.next
        #     l1 = l1.next if l1 else None
        #     l2 = l2.next if l2 else None

        #     # need to 
        # return dummy.next
        dummyHead = ListNode(0)
        tail = dummyHead
        carry = 0

        while l1 is not None or l2 is not None or carry != 0:
            digit1 = l1.val if l1 is not None else 0
            digit2 = l2.val if l2 is not None else 0

            sum = digit1 + digit2 + carry
            digit = sum % 10
            carry = sum // 10

            newNode = ListNode(digit)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next if l1 is not None else None
            l2 = l2.next if l2 is not None else None

        result = dummyHead.next
        dummyHead.next = None
        return result



solution = Solution()
linkedList1 = ListNode(2, ListNode(4,ListNode(3,None)))
linkedList2 = ListNode(5, ListNode(6,ListNode(4,None)))


res = solution.addTwoNumbers(linkedList1,linkedList2)


while res:
    print(res.val)
    res = res.next