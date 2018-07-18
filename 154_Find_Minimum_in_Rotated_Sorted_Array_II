"""
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.

(i.e.,  [0,1,2,4,5,6,7] might become  [4,5,6,7,0,1,2]).

Find the minimum element.

The array may contain duplicates.

Example 1:

Input: [1,3,5]
Output: 1
Example 2:

Input: [2,2,2,0,1]
Output: 0
Note:

This is a follow up problem to Find Minimum in Rotated Sorted Array.
Would allow duplicates affect the run-time complexity? How and why?
"""
class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """        
        start = 0;
        end = len(nums) - 1
        if len(nums) == 0:
            return -1;
        if len(nums) == 1:
            return nums[0]

        def helper(nums, start, end):
            if start == end:
                return nums[start]

            while start < end:
                mid = (start + end ) / 2
                s_num = nums[start]
                e_num = nums[end]
                m_num = nums[mid]
                if start + 1 == end:
                    return min(s_num, e_num)
                if s_num < e_num:
                    return s_num
                
                if s_num == e_num:
                    if m_num == e_num:
                        return min(helper(nums, mid, end), helper(nums, start, mid))
                if m_num >= s_num:                 
                    start = mid
                else:
                    end = mid

        return helper(nums, start, end)
