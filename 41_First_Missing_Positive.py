
"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

Good solution from discussion, but please note that be careful handl the index of list
Can't use nums[i], nums[nums[i]-1] = nums[nums[i]-1], nums[i] do the swap
"""
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l_n = len(nums)
        for i in range(l_n):
            while nums[i] >0 and nums[i] <= l_n and nums[i] != nums[nums[i]-1]:
                x = nums[i]
                y = nums[x-1]
                nums[i] = y
                nums[x-1] = x
        
        for i in range(l_n):
            if nums[i] != i+1:
                return i+1
        return l_n+1
            
