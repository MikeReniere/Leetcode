class Solution:
    def isPalindrome(self, s: str) -> bool:
        # NOTE: This solution works on flat python3 version, not whatever version im using
        # this solution is going to use pointers from the left and right of the string
        l, r = 0, len(s) - 1 # left and right pointers. L starts at 0, R starts at the end of the string

        while l < r:
            while l < r and not self.alphaNum(s[l]): # this makes sure the left character is alphanumeric. If its not then skip it and increment l
                l += 1
            while r > l and not self.alphaNum(s[r]):
                r -= 1
            if s[l].lower() != s[r].lower():
                return False
            l = l + 1
            r = r - 1
        return True

    def alphaNum(self,c):
        return (ord('A') <= ord(c) <= ord('Z') or ord('a') <= ord(c) <= ord('a'))  #ord gets the ascii value of the character
        # this is determining if the character is alphanumberic

solution = Solution()
s = "Was it a car or a cat I saw?"

print(solution.isPalindrome(s))