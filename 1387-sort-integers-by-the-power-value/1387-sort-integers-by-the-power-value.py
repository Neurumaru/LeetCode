from functools import cache

class Solution:
    @cache
    def dp(self, x: int) -> int:
        if x == 1:
            return 0
        if x % 2 == 0:
            return self.dp(x // 2) + 1
        else:
            return self.dp(3 * x + 1) + 1

    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted([(self.dp(x), x) for x in range(lo, hi+1)])[k-1][1]
