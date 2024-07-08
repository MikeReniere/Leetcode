def getMinErrors(errorString, x, y):
    MODULO = 1000000007
    n = len(errorString)
    
    # Initialize dp arrays
    dp0 = [float('inf')] * n  # dp0[i] represents the minimum errors up to i with ith character being '0'
    dp1 = [float('inf')] * n  # dp1[i] represents the minimum errors up to i with ith character being '1'
    
    # Base case for the first character
    if errorString[0] == '0':
        dp0[0] = 0
    elif errorString[0] == '1':
        dp1[0] = 0
    else:  # errorString[0] == '!'
        dp0[0] = 0
        dp1[0] = 0
    
    # Fill the dp arrays
    for i in range(1, n):
        if errorString[i] == '0':
            dp0[i] = min(dp0[i-1], dp1[i-1] + y)
        elif errorString[i] == '1':
            dp1[i] = min(dp1[i-1], dp0[i-1] + x)
        else:  # errorString[i] == '!'
            dp0[i] = min(dp0[i-1], dp1[i-1] + y)
            dp1[i] = min(dp1[i-1], dp0[i-1] + x)
    
    # The answer will be the minimum of the two possible states at the last character, taken modulo MODULO
    return min(dp0[n-1], dp1[n-1]) % MODULO

# Example usage:
errorString = "01!0"
x = 2
y = 3
print(getMinErrors(errorString, x, y))