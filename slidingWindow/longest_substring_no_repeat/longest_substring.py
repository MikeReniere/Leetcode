
class Solution:
    def lengthOfLongestSubstring(s: str) -> int:
        charSet = set()
        l = 0
        res = 0
        for r in range(len(s)):
            while s[r] in charSet: # when its a duplicate in our set
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            res = max(res,r-l + 1)
        return res
    
    s = "abcabcbb"
    print(lengthOfLongestSubstring(s))
