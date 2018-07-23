"""
Idea from discussion, which is easy to remember
Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]
Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]
Example 3:

Input: ")("
Output: [""]
"""

def removeInvalidParentheses(self, s):
    """
    :type s: str
    :rtype: List[str]
    """
    def isValid(s):
        s = filter("()".count, s)
        while s:
            n_s = s.replace("()", "")
            if s != n_s:
                s = n_s
            else:
                break
        return not s

    level = {s}
    while True:
        valid = filter(isValid, level)
        if valid:
            return valid
        temp = set()
        for l in level:
            for i in range(len(l)):
                temp.add(l[0:i] + l[i+1:])
        level = temp
