from typing import List

class Solution:
    def productExceptSelf(nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        # pre = [] * len(nums)
        # post = [] * len(nums)
        prefix = 1 # prefix default 1, which is the default number in th result output

        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]
        postfix = 1
        for i in range(len(nums) - 1, - 1, - 1): # this goes to the end of the array
            res[i] *= postfix # mutliples the post and prefix together
            postfix  *= nums[i] # basically just goes through the list backwards and multiples each value

        print(res)
        return res


    nums = [1,2,3,4]
    productExceptSelf(nums)