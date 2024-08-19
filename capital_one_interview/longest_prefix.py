from typing import List
class Solution:
    def longestCommonPrefix(arr1: List[int], arr2: List[int]) -> int:
        s = set()
        for x in arr1:
            while x:
                s.add(x)
                x //= 10
        ans = 0
        for x in arr2:
            while x:
                if x in s:
                    ans = max(ans, len(str(x)))
                    break
                x //= 10
        return ans
    
    print(longestCommonPrefix([1,10,100],[1000]))

    # time - O(mlogM + nlogn) 
    #memory - O(mLogm) 
    # m and n are the size of the arrays