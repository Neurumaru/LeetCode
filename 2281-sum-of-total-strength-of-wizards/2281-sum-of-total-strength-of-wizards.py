# 3
# lines: (3,1)
# cache: 3
# cache: 9
# 
#   4
# 3 3
# lines: (3,1) (4,1)
# cache: 3 7
# cahce: 9 37
#
#     1
#   1 1
# 1 1 1
# lines: (1,3)
# cache: 3
# cache: 14
# 
#       4
#     1 1
#   1 1 1
# 1 1 1 1
# lines: (1,3) (4,1)
# cache: 3 7
# cache: 14 42
# 
#         2
#       2 2
#     1 1 1
#   1 1 1 1
# 1 1 1 1 1
# lines: (1,3) (2,2)
# cache: 3 7
# cache: 14 34

class Solution:
    def totalStrength(self, strength: List[int]) -> int:
        prefix_sum1 = [0 for _ in range(len(strength)+1)]
        for i in range(len(strength)):
            prefix_sum1[i] = prefix_sum1[i-1] + strength[i]
        get_prefix_sum1 = lambda x, y : prefix_sum1[y] - prefix_sum1[x-1]
        prefix_sum2 = [0 for _ in range(len(strength)+1)]
        for i in range(len(strength)):
            prefix_sum2[len(strength)-i-1] = prefix_sum2[len(strength)-i] + strength[len(strength)-i-1] * (i+1)
        get_prefix_sum2 = lambda x, y : prefix_sum2[x] - prefix_sum2[y+1] - get_prefix_sum1(x, y) * (len(strength)-y-1)

        lines = []
        cache1 = []
        cache2 = []
        result = 0
        for i in range(len(strength)):
            value = strength[i]
            line = 1
            while lines and lines[-1][0] >= value:
                line += lines[-1][1]
                lines.pop()
                cache1.pop()
                cache2.pop()
            lines.append((value, line))
            cache1.append((value * line) + (cache1[-1] if cache1 else 0))
            cache = cache1[-1] * get_prefix_sum1(i-line+1, i) 
            cache -= value * get_prefix_sum2(i-line+1, i-1)
            cache2.append(cache + (cache2[-1] if cache2 else 0))
            result += cache2[-1]
            result %= 10**9 + 7
        return result