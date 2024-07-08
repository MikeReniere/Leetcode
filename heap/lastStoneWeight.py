from typing import List
import heapq
class Solution:
    def lastStoneWeight(stones: List[int]) -> int:
        # for python you neeed to use a min heap
        # and multiply every value by -1
        stones = [-s for s in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones) 

            if second > first: # this is second > first because they are all negative numbers 
                newStone = first - second # this is first - second (-8 - -7) = -1
                heapq.heappush(stones,newStone)

        if stones:
            return abs(stones[0]) #absolute value because its a negative value
        else:
            return 0

    print(lastStoneWeight([2,7,4,1,8,1]))