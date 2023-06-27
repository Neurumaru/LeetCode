from typing import List
from collections import deque

class BookMyShow:

    def __init__(self, n: int, m: int):
        self.book = [0 for _ in range(n)]
        self.col = m
        self.start_col = 0
        self.gather_cache = deque()
        self.gather_cache.append((0, m))
        self.gather_cache2 = dict()
        self.scatter_cache = dict()

    def _set_cache(self, i: int, k: int):
        start = 0
        mid = 0
        end = len(self.gather_cache)

        while start < end:
            mid = (start + end) // 2
            if self.gather_cache[mid][0] < i:
                start = mid + 1
            else:
                end = mid

        if 0 <= end-1 and self.gather_cache[end-1][1] > self.col - self.book[i] - k:
            return
        elif 0 <= end-1 and self.gather_cache[end-1][1] == self.col - self.book[i] - k:
            self.gather_cache[end-1] = (i, self.col - self.book[i] - k)
            if end < len(self.gather_cache) and self.gather_cache[end][0] == i:
                del(self.gather_cache[end])
            return

        if end < len(self.gather_cache) and self.gather_cache[end][0] == i:
            self.gather_cache[end] = (i, self.col - self.book[i] - k)
            return 
        
        while end < len(self.gather_cache) and self.gather_cache[end][1] < self.col - self.book[i] - k:
            del(self.gather_cache[end])

        self.gather_cache.insert(end, (i, self.col - self.book[i] - k))


    def _get_cache(self, k: int) -> int:
        start = 0
        end = len(self.gather_cache)

        while start < end:
            mid = (start + end) // 2
            if self.gather_cache[mid][1] < k:
                start = mid + 1
            elif self.gather_cache[mid][1] == k:
                break
            else:
                end = mid
        return self.gather_cache[mid][0]

    def gather(self, k: int, maxRow: int) -> List[int]:
        if maxRow in self.gather_cache2 and self.gather_cache2[maxRow] <= k:
            return []
        for i in range(self._get_cache(k), maxRow+1):
            if self.book[i] <= self.col - k:
                self._set_cache(i, k)
                self.book[i] += k
                return [i, self.book[i] - k]
        self.gather_cache2[maxRow] = k
        return []

    def scatter(self, k: int, maxRow: int) -> bool:
        if maxRow in self.scatter_cache and self.scatter_cache[maxRow] < k:
            return False
        cache = dict()
        result = False
        start_col = 0
        for i in range(self.start_col, maxRow+1):
            if self.book[i] <= self.col - k:
                self._set_cache(i, k)
                self.book[i] += k
                result = True
                break
            if self.book[i] < self.col:
                k -= self.col - self.book[i]
                cache[i] = self.col
                start_col = i + 1

        if result:
            self.start_col = start_col

            while self.gather_cache and self.gather_cache[0][0] < self.start_col:
                self.gather_cache.popleft()
            if not self.gather_cache:
                self.gather_cache.append((self.start_col, self.col - self.book[self.start_col]))

            for c in cache:
                self.book[c] = cache[c]
        else:
            self.scatter_cache[maxRow] = k
        return result