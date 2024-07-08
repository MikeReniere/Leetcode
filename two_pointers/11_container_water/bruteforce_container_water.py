from typing import List
class Solution:
    def maxArea(height: List[int]) -> int:
            # brute force way
        res = 0

        for l in range(len(height)): # left pointer goes from the 1st to the last point to check every single one
            for r in range(l + 1, len(hieght)): # for right pointer, in range of l+1 and length of height. This keeps it to the right of the left pointer
                area = (r-l) * min(height[l,r]) # width x height
                res = max(res, area)

        return res
    
                        
                  

        