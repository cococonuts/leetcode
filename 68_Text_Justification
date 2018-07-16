"""
Given an array of words and a width maxWidth, format the text such that each line has exactly maxWidth characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is, pack as many words as you can in each line. Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.

Extra spaces between words should be distributed as evenly as possible. If the number of spaces on a line do not divide evenly between words, the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:

    A word is defined as a character sequence consisting of non-space characters only.
    Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
    The input array words contains at least one word.

Example 1:

Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:

Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]
Explanation: Note that the last line is "shall be    " instead of "shall     be",
             because the last line must be left-justified instead of fully-justified.
             Note that the second line is also left-justified becase it contains only one word.

Example 3:

Input:
words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
Output:
[
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]


"""
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        lines = []
        width = 0
        line = []
        spaces = []
        for word in words:
            width += 1 + len(word)
            if width - 1 <= maxWidth:
                line.append(word)
            else:
                lines.append(line)
                line = []
                width = len(word) + 1
                line.append(word)
        if line not in lines:
            lines.append(line)
        
        for l in lines:
            w = 0
            for word in l:
                w = w +len(word)
            spaces.append(maxWidth-w)
                
        result = []
        for i in range(len(lines)):
            l = lines[i]
            print l
            if len(l) > 1 and i != (len(lines)-1):
                s = [spaces[i]/(len(l) - 1)] * len(l)
                for j in range(0, spaces[i] % (len(l) - 1)):
                    s[j+1] = s[j+1] + 1
                string = str(l[0])
                for i in range(1, len(l)):
                    string = string + ' '*s[i]
                    string = string + str(l[i])
                result.append(string)
            elif i == len(lines) -1: # last line
                string = str(l[0])
                for i in range(1, len(l)):
                    string = string + ' '
                    string = string + str(l[i])
                string = string + ' ' * (maxWidth - len(string))
                result.append(string)
            else:
                string = str(l[0]) + ' '*spaces[i]
                result.append(string)
        return result
