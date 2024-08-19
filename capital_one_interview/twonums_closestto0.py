# Given an array, find the sum of two integer closest to 0

def minAbsSumPair(arr):
    # Initialize left and right pointers, minimum sum, sum,
    # and minimum left and right indices
    l, r, min_sum, min_l, min_r = 0, 1, arr[0] + arr[1], 0, 1

    # Loop through the array
    for l in range(len(arr) - 1):
        # Inner loop to find the element with the minimum
        # sum
        for r in range(l + 1, len(arr)):
            # Calculate the sum of the current pair
            sum_pair = arr[l] + arr[r]

            # If the absolute value of the current sum is
            # less than the absolute value of the minimum
            # sum
            if abs(min_sum) > abs(sum_pair):
                # Update the minimum sum, minimum left and
                # right indices
                min_sum = sum_pair
                min_l, min_r = l, r

    # Return the sum of the two elements with the minimum
    # sum
    return arr[min_l] + arr[min_r]


print(minAbsSumPair([1, 60, -10, 70, -80, 85]))

# Initialize variables min_l and min_r to represent the indices of the pair with the minimum sum.
# Initialize min_sum with the sum of the first two elements (arr[0] + arr[1]).
# Run a loop l from 0 to n-1.
# Run a loop r from l+1 to n.
# For each pair of indices (l, r), calculate the sum of the corresponding elements (arr[l] + arr[r]).
# If the absolute value of the calculated sum is less than the absolute value of min_sum, update min_sum, min_l, and min_r with the current sum and indices.
# After completing the iteration, return the sum of the pair with indices min_l and min_r.