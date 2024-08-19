from typing import List
class Solution:
    def countAlternatingSubarrays(nums: List[int]) -> int:
        n = len(nums)
        count = 1
        start = 0
        
        for end in range(1, n):
            if nums[end] == nums[end-1]:
                start = end
            count += end - start + 1
        return count

        # O(n) time
        # O(1) space
    print(countAlternatingSubarrays([0,1,1,1])) # should return 5