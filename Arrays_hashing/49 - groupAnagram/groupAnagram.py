from typing import List
from collections import defaultdict 
class Solution:
    def groupAnagrams(strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # mapping Charcount : list of anagrams

        for s in strs:
            count = [0] * 26 # all 26 letters in the alphabet

            for c in s: 
                count[ord(c) - ord("a")] += 1  # this takes the ascii value of the current number, ord(a) - ord(a) = 0
                                          # ord(z) - ord(a) = 25 because its the 26th value in the alphabet
            res[tuple(count)].append(s) # lists cannot be keys in python

        return res.values()
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(groupAnagrams(strs))