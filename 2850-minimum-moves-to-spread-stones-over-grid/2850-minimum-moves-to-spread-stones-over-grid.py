from collections import deque
from typing import Dict, List


class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        def grid2hash(grid: List[List[int]]) -> int:
            res: int = 0

            for row in grid:
                for i in row:
                    res = res * 10 + i    

            return res

        def hash2grid(data: int) -> List[List[int]]:
            grid: List[List[int]] = [[0,0,0],[0,0,0],[0,0,0]]

            for i in range(3):
                for j in range(3):
                    grid[2-i][2-j] = data % 10
                    data = data // 10

            return grid

        q = deque()
        h: int = grid2hash(grid)
        dp: Dict[int, int] = dict()
        q.append(tuple([h, 0]))
        while q:
            h, m = q.popleft()
            zero_group: List[List[int]] = []
            multi_group: List[List[int]] = []
            for i, row in enumerate(hash2grid(h)):
                for j, data in enumerate(row):
                    if data == 0:
                        zero_group.append([i,j])
                    elif data > 1:
                        multi_group.append([i,j])
            
            for zero_i, zero_j in zero_group:
                for multi_i, multi_j in multi_group:
                    tmp_h = h
                    tmp_h += 10 ** (8 - (zero_i * 3 + zero_j))
                    tmp_h -= 10 ** (8 - (multi_i * 3 + multi_j))
                    tmp_m = m + abs(multi_i - zero_i) + abs(multi_j - zero_j)
                    if tmp_h in dp and dp[tmp_h] < tmp_m:
                        continue
                    
                    dp[tmp_h] = tmp_m
                    q.append(tuple([tmp_h, tmp_m]))
                    
        return dp[111111111]