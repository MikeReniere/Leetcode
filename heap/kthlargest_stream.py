from typing import List
import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.minHeap, self.k = nums, k
        heapq.heapify(self.minHeap) # turns minHeap into a heap

        while(len(self.minHeap)) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:
        heapq.heappush(self.minHeap, val) #heappop adds a value to the heap
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap) # removes the smallest value from the heap
        return self.minHeap[0] # min value is always stored in 0th index of a heap
    
obj = KthLargest(3, [4,5,8,2]) #3rd largest element 
param_1 = obj.add(9)

print(param_1)
param_2 = obj.add(10)
print(param_2)