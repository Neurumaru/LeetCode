from itertools import permutations

class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        zero_stones = []
        multi_stones = []

        for i in range(3):
            for j in range(3):
                if grid[i][j] == 0:
                    zero_stones.append([i, j])
                elif grid[i][j] > 1:
                    for k in range(grid[i][j]-1):
                        multi_stones.append(tuple([i, j]))

        min_l = 99999999
        for ms in set(permutations(multi_stones)):
            l = 0
            for i in range(len(zero_stones)):
                l += abs(zero_stones[i][0] - ms[i][0])
                l += abs(zero_stones[i][1] - ms[i][1])
            min_l = min(min_l, l)
        
        return min_l