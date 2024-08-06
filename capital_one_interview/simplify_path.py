class Solution:
    def simplifyPath(path: str) -> str:
        # time and memory is O(n) - just have to scan once, size of string is n 
        # memeory to create a simplified path (stack)
        #using a stack because of the ..
        stack = []
        curr = "" # current file or path that we are looking at

        for c in path + "/":
            if c == "/":
                if curr == "..":
                    if stack:
                        stack.pop()
                elif curr != "" and curr != ".":
                    stack.append(curr)
                curr = ""
            else: 
                curr += c

        # stack [abc, def]
        return "/" + "/".join(stack) # joins the stack together and adds a slash at the beginning

        

    path = path = "/home/user/Documents/../Pictures"
    print(simplifyPath(path))