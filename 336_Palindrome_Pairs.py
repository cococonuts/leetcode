"""
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list, so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]
Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
Credits:
Special thanks to @dietpepsi for adding this problem and creating all test cases.
"""

class Solution(object):
    def is_palindrome(self, word):
        return word == word[::-1]

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        dic = {}
        for i, word in enumerate(words):
            dic[word] = i

        result = set()
        for i, word in enumerate(words):
            if not word:
                for w in words:
                    if w != word and self.is_palindrome(w):
                        result.add((i, dic[w]))
                        result.add((dic[w], i))
            r_w = word[::-1]
            l_w = len(word)

            for j in range(1, l_w+1):
                n_w_1 = r_w[0:j]
                n_w_2 = r_w[j:]
                if n_w_2 in dic and i != dic[n_w_2]:
                    if self.is_palindrome(word+n_w_2):
                        result.add((i, dic[n_w_2]))
                if n_w_1 in dic and i != dic[n_w_1]:
                    if self.is_palindrome(n_w_1+word):
                        result.add((dic[n_w_1], i))
                        
        return list(result)
