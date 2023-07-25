from typing import Tuple
from functools import cache

class Solution:
    @cache
    def dp(self, target: int) -> int:
        if target == 0:
            return 0
        
        l = target.bit_length()
        
        if target == 2**l-1:
            return l
        
        tmp = []
        for i in range(l-1):
            # {l-1}R{i}R{dp()}
            tmp.append((l-1) + 1 + i + 1 + self.dp(target - (2**(l-1)-1) + (2**i-1)))
        # {l}R{dp()}
        tmp.append(l + 1 + self.dp((2**l-1) - target))
        return min(tmp)
        
    def racecar(self, target: int) -> int:
        return self.dp(target)
    
for i in range(100):
# i = 5
    print(f"{i}\t{Solution().dp(i)}")