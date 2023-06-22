class Solution:
    def specialPerm(self, nums: List[int]) -> int:
        matrix = [[False for i in range(len(nums))] for j in range(len(nums))]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i == j:
                    continue
                if nums[i] % nums[j] == 0:
                    matrix[i][j] = True
                elif nums[j] % nums[i] == 0:
                    matrix[i][j] = True
        primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43]
        is_visited = lambda visit, i: visit % primes[i] == 0
        prev_dp = [{primes[i]: 1} for i in range(len(nums))]
        for k in range(len(nums)-1):
            dp = [dict() for i in range(len(nums))]
            for i in range(len(nums)):
                for j in range(len(nums)):
                    if i == j:
                        continue
                    if matrix[i][j]:
                        for visit in prev_dp[j]:
                            if not is_visited(visit, i):
                                dp[i].setdefault(visit * primes[i], 0)
                                dp[i][visit * primes[i]] += prev_dp[j][visit]
            prev_dp = dp

        result = 0
        for i in range(len(nums)):
            for visit in prev_dp[i]:    
                result += prev_dp[i][visit]
            result %= 10 ** 9 + 7

        return result