from collections import deque

class Solution:
    def maximumRobots(self, chargeTimes: List[int], runningCosts: List[int], budget: int) -> int:
        def possible(k):
            queue = deque()
            for i in range(len(chargeTimes)):
                while queue and chargeTimes[queue[-1]] < chargeTimes[i]:
                    queue.pop()
                queue.append(i)
                if i < k-1:
                    continue
                if queue[0] == i-k:
                    queue.popleft()
                if chargeTimes[queue[0]] + k * get_prefix_sum(i-k+1, i) <= budget:
                    return True
            return False

        prefix_sum = [0 for _ in range(len(runningCosts)+1)]
        for i in range(len(runningCosts)):
            prefix_sum[i] = prefix_sum[i-1] + runningCosts[i]
        get_prefix_sum = lambda x,y : prefix_sum[y] - prefix_sum[x-1]
        
        start = 1
        end = len(runningCosts)+1
        result = 0

        while start < end:
            mid = (start + end) // 2
            print(mid, possible(mid))
            if possible(mid):
                result = mid
                start = mid + 1
            else:
                end = mid

        return result