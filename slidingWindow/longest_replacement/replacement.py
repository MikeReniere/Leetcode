class Solution:
    def characterReplacement(s: str, k: int) -> int:
        count = {}
        res = 0

        l = 0
        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r],0)
            
            # check if window is  valid
            while (r - l + 1 ) - max(count.values()) > k: # max.count(values) is the number of replacements needed
                count[s[l]] -= 1 # this decrements the count for "A" because we move past that value so it needs to be counted one less time
                                 # thus the sliding window!
                l += 1


            res = max(res,r - l + 1) # r-l + 1 is the length of the window
        return res
    
    s = "ABAB"
    k = 2
    print(characterReplacement(s,k))