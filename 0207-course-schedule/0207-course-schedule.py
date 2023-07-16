from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree, out_degree = dict(), dict()        
        for s, e in prerequisites:
            in_degree.setdefault(e, set())
            in_degree[e].add(s)
            out_degree.setdefault(s, set())
            out_degree[s].add(e)
        
        queue = deque()
        for i in range(numCourses):
            if i not in in_degree:
                queue.append(i)

        result = []
        while queue:
            s = queue.popleft()
            result.append(s)
            if s not in out_degree:
                continue
            for e in out_degree[s]:
                in_degree[e].remove(s)
                if not in_degree[e]:
                    queue.append(e)
            out_degree.pop(s)

        if len(result) != numCourses:
            return False
        return True