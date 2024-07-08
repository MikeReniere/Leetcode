class Solution:
    def isPalindrome(s: str) -> bool:
        newStr = ""
        for c in s:
            if c.isalnum(): # checks if its alphanumeric
                newStr += c.lower() # makes it all lower case
        return newStr == newStr[::-1] # this is how you reverse a string
   
    
    s = "A man, a plan, a canal: Panama"
    print(isPalindrome(s))

