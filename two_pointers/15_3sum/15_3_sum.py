from typing import List
class Solution:
    def threeSum(nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()

        for i, a in enumerate(nums):
            if i > 0 and a == nums[i - 1]: # this is checking if the value next to it is the same value that was used previously
                continue
            # 2 pointer solution (2sum II)
            l, r = i+1, len(nums) - 1
            while l < r:
                threeSum = a + nums[l] + nums[r]
                if threeSum > 0: 
                    r -=  1
                elif threeSum < 0:
                    l += 1
                else:
                    res.append([a,nums[l], nums[r]])
                    l += 1 # shifts the left pointer so it doesnt go through the loop an extra time
                    while nums[l] == nums[l - 1] and l < r: # this is the same value, keep shifting pointer
                        l += 1
        return res
    
    nums = [-1,0,1,2,-1,-4]
    print(threeSum(nums))