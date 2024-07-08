from typing import List
import heapq

class Solution:
    def findKthLargest(nums: List[int], k: int) -> int:
        # need to account for negative numbers 


        # this uses a maxheap
        nums = [-s for s in nums] # turns nums into a max heap where every value is negative
        heapq.heapify(nums) 

        i = 1
        while i != k:
            heapq.heappop(nums)
            i += 1
        
        return nums[0] * -1 # this turns the numbers back to their original state if they were negative or positive 


        


    
    
    #print(findKthLargest([3,2,1,5,6,4], 2)) # should return 5
    print(findKthLargest([-1,-1], 1))