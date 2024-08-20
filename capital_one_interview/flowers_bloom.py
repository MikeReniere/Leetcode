from typing import List
import heapq

class Solution:
    def fullBloomFlowers(flowers: List[List[int]], people: List[int]) -> List[int]:
        people = [(p, i) for i,p in enumerate(people)] #converts people into an array of pairs
        res = [0] * len(people)

        count = 0

        #initialize heaps
        start = [f[0]for f in flowers]
        end = [f[1]for f in flowers]

        heapq.heapify(start)
        heapq.heapify(end)

        for p, i in sorted(people): # counts for the person, based on their original index
            # how many flowers came into bloom before, or at the same time as the person arrived
            while start and start[0] <= p: # p is the time of the current person
                heapq.heappop(start) # this means a flower came into bloom before the person arrived
                count += 1
            while end and end[0] < p:  # flower went out of bloom 
                heapq.heappop(end)
                count -= 1


            res[i] = count

        return res
    
    # time complexity
    # O(mLogm + nLogn) - because of sorting
    
    # to optimize this
    # you can just use one heap
    # can just sort the array of flowers based on the starting interval
    
    print(fullBloomFlowers([[1,10],[3,3]],[3,3,2]))