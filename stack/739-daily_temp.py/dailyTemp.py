from typing import List

class Solution:
    def dailyTemperatures(temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = [] # pair of values, [temperature, index from temperatures of value]

        for i, t in enumerate(temperatures): # is index, t is temperature
            
            while stack and t > stack[-1][0]: # while stack is not empty and current temperate is greater than the top of the stack 
                                               # stack[-1] (top of stack) [0] is the first value in that pair
                stackT, stackInd = stack.pop()
                res[stackInd] = (i - stackInd) # current index of temperature value - the stackIndex (from the pair of values in the stack)
            stack.append([t,i])
        return res
        

    print(dailyTemperatures([73,74,75,71,69,72,76,73])) # output should be [1,1,4,2,1,1,0,0]

