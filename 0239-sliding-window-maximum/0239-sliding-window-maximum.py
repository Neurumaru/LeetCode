# 시간 복잡도 : O(nlogn)
# 공간 복잡도 : O(nlogn)
# DP를 사용해서 해결
# k+1 // 2의 값들을 이용해 k의 값을 구하는 방식을 재귀해서 사용

class Solution:
    def calcMaxValues(self, k):
        use_k = (k+1) // 2
        len_k = len(self.max_values[1]) - k + 1
        if use_k not in self.max_values:
            self.calcMaxValues(use_k)
        
        self.max_values.setdefault(k, [0 for _ in range(len_k)])
        for i in range(len_k):
            self.max_values[k][i] = max(
                self.max_values[use_k][i], 
                self.max_values[use_k][i+use_k if k % 2 == 0 else i+use_k-1]
            )

    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # key=k, value=k에 해당하는 slice들의 max_values
        self.max_values = {1: nums}
        self.calcMaxValues(k)

        return self.max_values[k]
