"""
It is not the perfect solution. But after I tried many times. It is finally resolved. Haha
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        p = p[::-1]
        s = s[::-1]
        
        return self.match(s, p)
        
    def match(self, s, p):    
        l_s = len(s)
        l_p = len(p)
        
        i_s = 0
        i_p = 0
        if s == p:
            return True
        if s == '':
            while(i_p < l_p and p[i_p] =="*"):
                i_p += 2
    
        while i_s < l_s:
            if i_p < l_p and (p[i_p] == "." or p[i_p] == s[i_s]):
                i_p += 1
                i_s += 1
            elif i_p < l_p and p[i_p] == "*":
                if i_p + 1 < l_p:
                    c = p[i_p+1]
                    if self.match(s[i_s:], p[i_p+2:]):
                        return True
                    else:
                        while i_s < l_s:
                            i_s += 1
                            if c == s[i_s-1] or c == '.':
                                if self.match(s[i_s:], p[i_p+2:]):
                                    return True
                            else:
                                return False
            else:
                return False
        if i_s == l_s:
            while(i_p < l_p and p[i_p] =="*"):
                i_p += 2
        return i_p == l_p and  i_s == l_s
