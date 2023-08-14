from typing import List
from functools import cache

class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        @cache
        def dp(i: int, j: int) -> int:
            if j-i == 1:
                return 0
            if j-i == 2:
                return nums[i] * nums[i+1] * nums[j]
            return max([nums[i]*nums[k]*nums[j]+dp(i,k)+dp(k,j) for k in range(i+1, j)])
        return dp(0,len(nums)-1)
            