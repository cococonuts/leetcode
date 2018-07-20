"""
The idea is from ++ ^_^

Given an m x n matrix of positive integers representing the height of each unit cell in a 2D elevation map, compute the volume of water it is able to trap after raining.

Note:
Both m and n are less than 110. The height of each unit cell is greater than 0 and is less than 20,000.

Example:

Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]

Return 4.
"""
class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap:
            return 0

        dirs = [[-1, 0], [0, 1], [1, 0], [0, -1]]
        
        len_v = len(heightMap)
        len_h = len(heightMap[0])
        heap = []
        visit = [[0 for i in range(len_h)] for j in range(len_v)]
        for i in range(len_v):
            heapq.heappush(heap, (heightMap[i][0], i, 0))
            heapq.heappush(heap, (heightMap[i][len_h-1], i, len_h-1))
            visit[i][len_h-1] = 1
            visit[i][0] = 1
        for j in range(len_h):
            heapq.heappush(heap, (heightMap[0][j], 0, j))
            heapq.heappush(heap, (heightMap[len_v-1][j], len_v-1, j))
            visit[0][j] = 1
            visit[len_v-1][j] = 1
        
        current_max = 0
        result = 0
        while len(heap) > 0:
            (height, i, j) = heapq.heappop(heap)
            current_max = max(current_max, height)
            for dir in dirs:
                n_i = i + dir[0]
                n_j = j + dir[1]
                if n_i >= 0 and n_i < len_v and n_j >= 0 and n_j < len_h and visit[n_i][n_j] == 0:
                    heapq.heappush(heap, (heightMap[n_i][n_j], n_i, n_j))
                    visit[n_i][n_j] = 1
                    result += current_max - heightMap[n_i][n_j]  if current_max - heightMap[n_i][n_j] > 0 else 0
        return result
