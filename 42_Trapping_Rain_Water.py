"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        temp = []
        m = 0
        for i in range(len(height)):
            m = max(height[i], m)
            temp.append(m)
        
        m = 0
        for i in reversed(range(len(height))):
            m = max(height[i], m)
            temp[i] = min(m, temp[i])
        
        result = 0
        for i in range(len(height)):
            if (temp[i] - height[i]) > 0:
                result += temp[i] - height[i]
        return result
