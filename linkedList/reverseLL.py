class ListNode:    
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next



class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        # iteratively  
        prev, curr =  None, head

        while curr: 
            nxt = curr.next # temp value of nxt 
            curr.next = prev # 
            prev = curr #update pointers by moving them to the right
            curr = nxt
        return prev
    
solution = Solution()
linkedList = ListNode(0, ListNode(2,ListNode(3,ListNode(4,None))))
res = solution.reverseList(linkedList)

while res:
    print(res.val)
    res = res.next


