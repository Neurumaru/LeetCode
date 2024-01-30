# ayaan.jun
class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        s2d: Dict[int, Set[int]] = {i: set() for i in range(n)}
        d2s: Dict[int, Set[int]] = {i: set() for i in range(n)}

        for source, destination in relations:
            s2d[source-1].add(destination-1)
            d2s[destination-1].add(source-1)

        tmp: Set[int] = set()
        for destination in d2s:
            if len(d2s[destination]) == 0:
                tmp.add(destination)

        step: int = 0
        visit: int = 0
        complete: int = 2 ** n - 1
        while tmp and visit != complete:
            next_tmp: Set[int] = set()
            
            for source in tmp:
                visit |= 1 << source
                for destination in s2d[source]:
                    if sum([visit & 1 << need == 0 for need in d2s[destination]]) == 0:
                        next_tmp.add(destination)

            tmp = next_tmp
            step += 1

        if visit != complete:
            return -1
            
        return step
            