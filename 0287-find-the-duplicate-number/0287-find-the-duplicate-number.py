from typing import List

class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        tmp = 0
        while True:
            tmp = nums[tmp]
            slow = nums[slow]
            if tmp == slow:
                return tmp