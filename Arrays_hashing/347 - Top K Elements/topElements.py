from typing import List
from collections import Counter

class Solution:
    def topKFrequent(nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1 )] # freq is list of lists that is the same length as nums

        for numbers in nums: 
            count[numbers] = 1 + count.get(numbers, 0)
        for n, c in count.items(): # number: counnt  number is number 
            freq[c].append(n) # count n occurs exactly c number of times -- this appends the number value to the index of how many times it occured 
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]: # for n in freq[i] which is a list!!!!
                res.append(n)
                if len(res) == k:
                    return res
                
    print(topKFrequent([1,1,1,2,2,3], 2))