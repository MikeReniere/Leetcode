from typing import List
class Solution:   
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        h = {}
        freq = [[] for i in range(len(nums) + 1)]

        for i in nums:
            h[i] = 1 + h.get(i,0)
            # if i not in h:
            #     h[i] = 1
            # else: 
            #     h[i] += 1
        for n, c in h.items(): #number, count
            freq[c].append(n)
                
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

    
    nums = [1,2,2,3,3,3] 
    k = 2

    print(topKFrequent(nums,k))
