from typing import List
class Solution:
    def findMin(nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        res = nums[0]

        while l <= r:
            if nums[l] < nums[r]: # if l is less than r (in the current portion) 
                res = min(res,nums[l]) # gets the minimum value 
                break

            midPoint = (l+r) //2
            res = min(res, nums[midPoint])

            if nums[midPoint] >= nums[l]:  # this means the midpoint is a part of the left sorted portion, so we want to search to the right
                l = midPoint+1
            else:
                r = midPoint - 1
        return res

        

    
    nums = [3,4,5,1,2]
    print(findMin(nums))
