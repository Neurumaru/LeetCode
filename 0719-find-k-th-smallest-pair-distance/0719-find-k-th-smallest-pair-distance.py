# 시간 복잡도 : O(nlogn)
# 공간 복잡도 : O(1)

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        nums.sort()

        start = 0
        end = nums[-1]

        while start <= end:
            mid = (start + end) // 2
            data, curr = 0, 0
            for i in range(len(nums)):
                while nums[i] - nums[curr] > mid:
                    curr += 1
                data += i - curr
            if data >= k:
                end = mid - 1
            else:
                start = mid + 1
        return start