class Solution:
    def totalSteps(self, nums: List[int]) -> int:
        max_num = 0
        max_con = 0
        stack = []
        for num in nums:
            if max_num <= num:
                max_num = num
                max_con = max(max_con, [n for m, n in stack])
                stack = []

            max_n = 0
            while stack and stack[-1][0] <= num:
                m, n = stack.pop()
                max_n = max(max_n, n)
            stack.append((num, max_n + 1))
        return max_con
