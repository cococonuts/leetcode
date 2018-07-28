"""
Note: try to remove duplicate nums
Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
"""
class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        l_nums = len(nums)
        for i in range(l_nums):
            if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                target = 0 - nums[i]
                start = i + 1
                end = l_nums - 1
                temp = []
                while start < end:
                    sum = nums[start] + nums[end]
                    if sum > target:
                        end -= 1
                    elif sum < target:
                        start += 1
                    else:
                        temp.append(nums[start])
                        temp.append(nums[end])
                        temp.append(nums[i])
                        result.append(temp)
                        temp = []
                        while start < end and nums[start] == nums[start+1]:
                            start += 1
                        while start < end and nums[end] == nums[end-1]:
                            end -= 1
                        start += 1
                        end -= 1
        return result
