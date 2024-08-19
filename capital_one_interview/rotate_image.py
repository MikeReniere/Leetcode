from typing import List
class Solution:
    def rotate(matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l, r = 0, len(matrix) - 1

        while l < r:
            for i in range(r - l): # iterate through entire row except last element
                top,bottom = l, r

                #save the top left value 
                topLeft = matrix[top][l + i]

                #move bottom left into top left
                matrix[top][l + i] = matrix[bottom - i][l]

                # move bot right to bot left
                matrix[bottom - i][l] = matrix[bottom][r - i]

                #move top right into bottom left
                matrix[bottom][r - i] = matrix[top + i][r]

                # move top left into top right
                matrix[top + i][r] = topLeft


            #update pointers for sub matrix
            r -= 1
            l += 1






    matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]] 
    print(rotate(matrix))

#o(n^2) time
#o(1) mem - because we are doing this in place