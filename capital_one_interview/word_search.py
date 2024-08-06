from typing import List

class Solution:
    def exist(board: List[List[str]], word: str) -> bool:
        # time complexity: O(n * m * dfs(4^n)) -- n * m (dimensions of the board)
        # this uses brute force, DFS on the board
        ROWS, COLS = len(board), len(board[0])
        path = set() # this adds current values so we cant use a variable that was used in the path previously


        def dfs(r,c,i): #r,c are coordinates, i is  the current character in our target word 
            if i == len(word): # if word is done
                return True
            if (r < 0 or c < 0 or # if we're out of bounds
                r >= ROWS or c >= COLS or # r or c are more than the number of rows or columns
                word[i] != board[r][c] or  # found the wrong character 
                (r,c) in path): # this means we're visiting the same position twice 
                return False
            path.add((r,c)) # adds the position to the path
            res = (dfs(r + 1, c, i+1) or 
                    dfs(r - 1, c, i+1) or 
                    dfs(r, c+1, i+1) or 
                    dfs(r, c-1, i+1)) # this checks all 4 adjactent positons, if it returns true, we get the target word and it will return true
            path.remove((r,c))
            
            return res
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r,c,0):
                    return True
        return False




    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    print(exist(board, "ABCCED"))