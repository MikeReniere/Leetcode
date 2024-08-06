from typing import List
class Solution:
    def twoSum(nums: List[int], target: int) -> List[int]:
        h = {}
        
        for i, n in enumerate(nums): # i is index, n is value from nums
            difference = target - n
            if difference in h:
                return [h[difference], i]
            h[n] = i


    nums = [5,2,1,5,3]
    print(twoSum(nums, 4))