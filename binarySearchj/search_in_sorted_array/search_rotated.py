from typing import List
class Solution:
    def search(nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1

        while l <= r:
            midPoint = (l + r) // 2
            if target == nums[midPoint]:
                return midPoint

            if nums[l] <= nums[midPoint]: # initially search the right portion
                if target > nums[midPoint] or target < nums[l]:
                    l = midPoint + 1
                else:  # that means the target is less than middle, but greater than the left (so its in the left section)
                    r = midPoint - 1
            else: #this means search the right sorted portion
                if target < nums[midPoint] or target > nums[r]:
                    r = midPoint -1
                else: 
                    l = midPoint
            
        return -1


            # if nums[midPoint] > target and target > r :
            #     r = midPoint - 1
            # if nums[midPoint] < target and target < r:
            #     l = midPoint + 1
    

        

    nums = [4,5,6,7,0,1,2]
    target = 0
    print(search(nums,target))      