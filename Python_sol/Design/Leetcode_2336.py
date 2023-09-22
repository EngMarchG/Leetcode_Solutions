class SmallestInfiniteSet:

    def __init__(self):
        self.nums = set()
        self.smallest = 1

    def popSmallest(self) -> int:
        while self.smallest in self.nums:
            self.smallest += 1
        self.nums.add(self.smallest)
        return self.smallest

    def addBack(self, num: int) -> None:
        if num < self.smallest:
            self.smallest = num
        self.nums.discard(num)
        


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()