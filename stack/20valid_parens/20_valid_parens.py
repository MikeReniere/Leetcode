class Solution:
    def isValid(s: str) -> bool:
        stack = []
        closeToOpen = {")" : "(", "]":"[", "}":"{"}

        for c in s:
            if c in closeToOpen: # if it is an open paranthesis  (if its a key in closeToOpen)
                if stack and stack[-1] == closeToOpen[c]: #stack[-1] is the last value we added to the stack
                    stack.pop()
                else:
                    return False
            else: # this is if we get an open parenthesis
                stack.append(c)
            
        return True if not stack else False
    
    #s = "()[]{}"
    s = "((([[[]]])))"
    print(isValid(s))


    