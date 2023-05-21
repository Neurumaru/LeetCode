# 시간 복잡도 : O(nlogn) ~ O(n^2)
# 공간 복잡도 : O(n)

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        result = 1
        prev_end = 0
        while intervals:
            del_i = len(intervals)

            # ============================================================
            # Solution 1 : 최악의 경우 O(n)이지만 일반적으로 짧게 걸림
            # for i, (start, end) in enumerate(intervals):
            #     if start >= prev_end:
            #         del_i = i
            #         break
            # ============================================================
            # Solution 2 : 일반적으로 O(logn)이지만 일반적으로 오래 걸림
            s = 0
            e = len(intervals) - 1
            while s <= e:
                m = (s + e) // 2
                if intervals[m][0] == prev_end:
                    del_i = m
                    break
                elif intervals[m][0] < prev_end:
                    s = m + 1
                else:
                    e = m - 1
            del_i = s
            # ============================================================

            if del_i == len(intervals):
                prev_end = intervals[0][1]
                result += 1
                del(intervals[0])
            else:
                prev_end = intervals[del_i][1]
                del(intervals[del_i])

        return result