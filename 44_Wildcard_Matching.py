"""
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:

    s could be empty and contains only lowercase letters a-z.
    p could be empty and contains only lowercase letters a-z, and characters like ? or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""
    
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        pattern = re.sub(r'(\d)\1+', r'\1', p)
        if s == '' and p == '':
            return True

        i_s = 0
        i_p = 0
        l_s = len(s)
        l_p = len(p)
        match = 0
        star = -1
        while i_s < l_s:
            if i_p < l_p and (p[i_p] == s[i_s] or p[i_p] == '?'):
                i_p += 1
                i_s += 1
            elif i_p < l_p and p[i_p] == "*":
                match = i_s
                star = i_p
                i_p += 1
            elif star >= 0:
                match += 1
                i_s = match
                i_p = star + 1
            else:
                return False
            
        while i_p < l_p and p[i_p] == '*':
            i_p += 1
        return i_p == l_p
