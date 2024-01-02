from typing import List, Set


class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        abj_list: List[Set[int]] = [{i} for i in range(len(bombs))]
        abj_from: List[Set[int]] = [set() for i in range(len(bombs))]

        for i, (x1, y1, r1) in enumerate(bombs):
            for j, (x2, y2, _) in enumerate(bombs):
                if i == j:
                    continue

                if (x1 - x2) ** 2 + (y1 - y2) ** 2 <= r1**2:
                    abj_list[i].add(j)
                    abj_from[j].add(i)

        q: Set[int] = {i for i in range(len(bombs))}
        while q:
            i: int = q.pop()
            tmp: int = len(abj_list[i])
            for j in abj_list[i].copy():
                abj_list[i].update(abj_list[j])
            if len(abj_list[i]) == tmp:
                continue
            for j in abj_from[i]:
                q.add(j)

        return max([len(abj) for abj in abj_list])
