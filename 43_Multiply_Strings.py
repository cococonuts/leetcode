"""
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"
Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"
Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        if not num1 or num1 =='0' or not num2 or num2 == '0':
            return "0"

        n1 = num1[::-1] 
        n2 = num2[::-1]

        def add_str(x1, x2):
            if not x1:
                return x2
            if not x2:
                return x1

            add = 0
            result = ""
            x = x1[::-1] if len(x1) > len(x2) else x2[::-1]
            y = x2[::-1] if len(x1) > len(x2) else x1[::-1]
            index = 0
            while index < len(y):
                sum = int(x[index]) + int(y[index]) + add
                add = 1 if sum > 9 else 0
                sum = sum % 10
                result = str(sum) + result
                index += 1
            
            for i in range(index, len(x)):
                sum = add + int(x[i])
                add = 1 if sum > 9 else 0
                sum = sum % 10
                result = str(sum) + result
            if add:
                result = str(add) + result
            return result
            
        add = 0
        result = ""
        for i, c1 in enumerate(n1):
            temp = ''
            for j, c2 in enumerate(n2):
                num = int(c1) * int(c2) + add
                add = num / 10
                num = num % 10
                temp = str(num) + temp
            if add:
                temp = str(add) + temp
            add = 0
            temp += "0" * i
            result = add_str(temp, result)

        return result
