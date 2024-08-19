from typing import List

class Solution:
    def fullJustify(words: List[str], maxWidth: int) -> List[str]:
        res = []  # array where each value is each line in the output
        line = []  # Words in current line
        length = 0  # Current line length
        i = 0 # pointer so we loop through the entire input 
        while i < len(words):
            if length + len(line) + len(words[i]) > maxWidth:
                 # curr line is complete
                # distrubute extra space evenly
                # Line complete
                extra_space = maxWidth - length
                word_cnt = len(line) - 1
                spaces = extra_space // max(1, word_cnt) # - 1because we put the spaces inbetween words, not at the end
                                                                # max() is for the edge case where length of the line is 1, so we dont get divide by 0 error
                
                remainder = extra_space % max(1, word_cnt)  # get the value to distrbute left -> right

                for j in range(max(1, len(line) - 1)): # currLine contains all words have in the current line. -1 is so we dont add space at the end of the words
                                                        # max handles the same edge case as above
                    line[j] += " " * spaces
                    if remainder:
                        line[j] += " "
                        remainder -= 1

                res.append("".join(line))
                line, length = [], 0  # Reset line and length
            
             # line is not complete
            line.append(words[i])
            length += len(words[i])
            i += 1

        # Handling the last line
        last_line = " ".join(line)
        trail_spaces = maxWidth - len(last_line)
        res.append(last_line + (trail_spaces * " "))

        return res


    words = ["This", "is", "an", "example", "of", "text", "justification."]
    print(fullJustify(words, 16))