from bisect import insort
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        graph = dict()
        for start, end in tickets:
            graph.setdefault(start, [])
            insort(graph[start], end)
        result = []
        def dfs(node):
            while node in graph and graph[node]:
                dfs(graph[node].pop(0))
            result.append(node)
        dfs("JFK")
        return result[::-1]