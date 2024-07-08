from typing import List

class Solution:
    def search(nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 # 0, and last index

        while l <= r:
            mid = (l + r) // 2 # midwa7y point
            if nums[mid] > target:
                r = mid-1
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
        return -1     
        
    nums = [-1,0,3,5,9,12]
    target = 9
    print(search(nums,target))
