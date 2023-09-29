from typing import List
from bisect import insort

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        smaller = nums1 if len(nums1) <= len(nums2) else nums2
        larger = nums2 if len(nums1) <= len(nums2) else nums1
        if len(smaller) == 0:
            if len(larger) % 2 == 0:
                return (larger[len(larger) // 2] + larger[len(larger) // 2 - 1]) / 2
            else:
                return larger[len(larger) // 2]
        elif len(smaller) == 1:
            insort(larger, smaller[0])
            if len(larger) % 2 == 0:
                return (larger[len(larger) // 2] + larger[len(larger) // 2 - 1]) / 2
            else:
                return larger[len(larger) // 2]

        s, e = 0, len(smaller)
        while s < e:
            sm = (s + e) // 2
            lm = (len(larger) + len(smaller)) // 2 - sm - 1
            print(sm, lm)
            if smaller[sm] < larger[lm]:
                s = sm + 1
            else:
                e = sm

        if e == 0:
            if len(smaller) == len(larger):
                return (smaller[0] + larger[-1]) / 2
            if (len(smaller) + len(larger)) % 2 == 0:
                if smaller[0] < larger[lm+1]:
                    return (smaller[0] + larger[lm]) / 2
                return (larger[lm] + larger[lm+1]) / 2
            if smaller[e] < larger[lm+1]:
                return smaller[e]
            return larger[lm+1]
        if e == len(smaller):
            if len(smaller) == len(larger):
                return (smaller[-1] + larger[0]) / 2
            if (len(smaller) + len(larger)) % 2 == 0:
                if smaller[-1] > larger[lm-1]:
                    return (smaller[-1] + larger[lm]) / 2
                return (larger[lm-1] + larger[lm]) / 2
            return larger[lm]
        else:
            sm = e
            lm = (len(larger) + len(smaller)) // 2 - e - 1
            mid = sorted([smaller[sm], smaller[sm-1], larger[lm], larger[lm+1]])
            front = (sm-1) + lm
            back = len(smaller) - (sm+1) + len(larger) - (lm+2)

            if front == back:
                return (mid[1] + mid[2]) / 2
            return mid[2]
