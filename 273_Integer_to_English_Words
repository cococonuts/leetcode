"""
273. Integer to English Words
Convert a non-negative integer to its english words representation. Given input is guaranteed to be less than 231 - 1.

Example 1:

Input: 123
Output: "One Hundred Twenty Three"

Example 2:

Input: 12345
Output: "Twelve Thousand Three Hundred Forty Five"

Example 3:

Input: 1234567
Output: "One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven"

Example 4:

Input: 1234567891
Output: "One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninet
"""
class Solution(object):
    def get_str(self, num):
        num_word_dict_20_100 = {90:"Ninety", 80:"Eighty", 70:"Seventy", 60:"Sixty", 50:"Fifty", 40:"Forty", 30:"Thirty", 20:"Twenty"}
        num_word_dict_1_19 = {19:"Nineteen", 18:"Eighteen", 17:"Seventeen", 16:"Sixteen", 15:"Fifteen", 14:"Fourteen", 13:"Thirteen", 12:"Twelve", 11:"Eleven", 10:"Ten", 9:"Nine", 8:"Eight", 7:"Seven", 6:"Six", 5:"Five", 4:"Four", 3:"Three", 2:"Two", 1:"One"}
        
        result = ''
        if num < 1000:
            if num / 100 > 0:
                result += num_word_dict_1_19[num/100] + " " + "Hundred"
                num = num % 100
            if num/10 * 10 in num_word_dict_20_100:
                result += " " + num_word_dict_20_100[num/10 * 10]
                if num - num/10 * 10 in num_word_dict_1_19:
                    result += " " + num_word_dict_1_19[num - num/10 * 10]
            elif num in num_word_dict_1_19:
                result += " " + num_word_dict_1_19[num]
                
        else:
            return ""
        return result
    def numberToWords(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return "Zero"
    
        num_word_dict = {1000000000:"Billion", 1000000:"Million", 1000:"Thousand"}
        
        result = ""
        for key in sorted(num_word_dict, reverse=True):
            if num / key > 0:
                if result:
                    result += " "
                result += self.get_str(num/key).lstrip()
                result += " "
                result += num_word_dict[key]
            num = num % key
        if num > 0:
            result += " " + self.get_str(num).lstrip()
        return result.lstrip()
