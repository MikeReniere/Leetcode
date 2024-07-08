from typing import List

class Solution:
    def longestConsecutive(nums: List[int]) -> int:
        numSet = set(nums)
        longest = 0

        for n in nums:
            # check if its the start of a sequence
            if (n - 1) not in numSet:
                length = 0 # length of current sequence
                while (n + length) in numSet: 
                    length += 1 # adds one to the current sequence if n + length exists 
                longest = max(length,longest)
        print(longest)
        return longest
                    


    nums = [100,4,200,1,3,2]
    longestConsecutive(nums)