from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        curr = 1
        while curr < len(nums):
            if nums[curr-1] != nums[curr]:
                del(nums[curr-1])
                del(nums[curr-1])
                if curr - 1 > 0:
                    curr -= 1
                continue
            curr += 1
        return nums[0]