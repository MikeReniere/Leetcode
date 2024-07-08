from typing import List
class Solution:
    def maxArea(height: List[int]) -> int:
        # Linear time solution O(n) because we only go through the array once
        l, r = 0, len(height) -1
        res = 0

        while l < r:
            area = (r-l) * min(height[l], height[r]) # width x height
            res = max(res, area)
            if height[l] > height[r]:
                r -= 1   
            elif height[l] < height[r]:
                l += 1
            else: 
                r -= 1
        return res


    
    height = [1,8,6,2,5,4,8,3,7]
    print(maxArea(height))