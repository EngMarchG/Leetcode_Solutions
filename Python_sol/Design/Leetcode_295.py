class MedianFinder:

    def __init__(self):
        self.arr = []
        self.median = None
        self.flag = 0

    def addNum(self, num: int) -> None:
        if self.arr:
            if self.arr[-1]<=num:
                self.arr.append(num)
                return
            elif self.arr[0]>num:
                self.arr.insert(0,num)
                return
        self.arr.append(num)
        self.flag = 1

    def findMedian(self) -> float:
        if self.flag:
            self.arr = sorted(self.arr)
            self.flag = 0

        if len(self.arr)%2:
            return self.arr[len(self.arr)//2]
        elif len(self.arr):
            return (self.arr[len(self.arr)//2]+self.arr[len(self.arr)//2 -1])/2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()