from typing import List

class Solution:
    def twoSum(numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 # left and right pointers
        
        while l < r:
            curSum = numbers[l] + numbers[r]
            
            if curSum < target:
                l += 1
            elif curSum > target:
                r -= 1
            else:
                return [l + 1, r + 1]

    numbers = [2,7,11,15]
    print(twoSum(numbers, 9))


