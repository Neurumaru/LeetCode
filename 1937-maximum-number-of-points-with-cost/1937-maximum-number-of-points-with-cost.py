from typing import List

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        dp = points[0]
        for row in range(1, len(points)):
            local_max = 0
            for col in range(len(dp)):
                local_max = max(local_max-1, dp[col])
                dp[col] = max(dp[col], local_max)
            
            local_max = 0
            for col in reversed(range(len(dp))):
                local_max = max(local_max-1, dp[col])
                dp[col] = max(dp[col], local_max)

            for col in range(len(dp)):
                dp[col] += points[row][col]
        return max(dp)
    