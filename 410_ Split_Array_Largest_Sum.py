"""
Pretty cool solution from discussion, not by me : (
Given an array which consists of non-negative integers and an integer m, you can split the array into m non-empty continuous subarrays. Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)
Examples:

Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.
"""
class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        max_num = 0
        sum = 0
        for num in nums:
            max_num = max(max_num, num)
            sum += num
        
        if m == 1:
            return sum

        left = max_num
        right = sum
        def isValid(target, m, nums):
            sum = 0
            count = 1
            for num in nums:
                sum += num
                if sum > target:
                    sum = num
                    count += 1
                    if count > m:
                        return False
            return True
        while left <= right:
            mid = (left + right) / 2
            if isValid(mid, m ,nums):
                right = mid -1
            else:
                left = mid + 1
        return left
