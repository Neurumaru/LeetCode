class MedianFinder:

    def __init__(self):
        self.nums = 0
        self.histogram100 = {}
        self.histograms = {}

    def addNum(self, num: int) -> None:
        self.histogram100.setdefault(num // 100, 0)
        self.histograms.setdefault(num // 100, {})
        self.histograms[num // 100].setdefault(num % 100, 0)

        self.nums += 1
        self.histogram100[num // 100] += 1
        self.histograms[num // 100][num % 100] += 1

    def findMedian(self) -> float:
        sum_num = 0
        pre_key100 = None
        for key100 in sorted(self.histogram100.keys()):
            sum_num += self.histogram100[key100]
            if sum_num > self.nums // 2:
                break
            pre_key100 = key100

        sum_num -= self.histogram100[key100]
        pre_key = None
        for key in sorted(self.histograms[key100].keys()):
            sum_num += self.histograms[key100][key]
            if sum_num > self.nums // 2:
                break
            pre_key = key
        
        if self.nums % 2 == 1:
            return key100 * 100 + key
        sum_num -= self.histograms[key100][key]
        if sum_num == self.nums // 2:
            if pre_key != None:
                return key100 * 100 + (key + pre_key) / 2.0
            return (pre_key100 + key100) * 50 + (key + max(self.histograms[pre_key100].keys())) / 2.0
        return key100 * 100 + key
        
