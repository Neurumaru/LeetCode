class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == "1":
                    queue = []
                    queue.append((i, j))

                    while len(queue) > 0:
                        m, n = queue.pop()
                        grid[m][n] = "0"
                        if 0 < m and grid[m-1][n] == "1":
                            queue.append((m-1, n))
                        if m < len(grid) - 1 and grid[m+1][n] == "1":
                            queue.append((m+1, n))
                        if 0 < n and grid[m][n-1] == "1":
                            queue.append((m, n-1))
                        if n < len(grid[m]) - 1 and grid[m][n+1] == "1":
                            queue.append((m, n+1))

                    count += 1

        return count
