class SummaryRanges:

    def __init__(self):
        self.arr = []
        self.interval = []

    def addNum(self, value: int) -> None:
        # Sort the new added number by swapping from end to start
        if len(self.arr)>1:
            if value>self.arr[-1]:
                self.arr.append(value)
            else:
                for i in range(len(self.arr)-1):
                    if self.arr[i]<value and self.arr[i+1]>value:
                        self.arr.insert(i,value)
                        break
        else:
            self.arr.append(value)

        if not self.interval and self.arr:
            self.interval.append([self.arr[0],self.arr[0]])
        else:
            for i in range(len(self.interval)):
                if self.interval[i][0]-value==1:
                    self.interval[i][0] = value
                    break
                elif self.interval[i][0]<=value<=self.interval[i][1]:
                    break
                elif (value - self.interval[i][1])==1:
                    if i+1<len(self.interval) and self.interval[i+1][0]-value==1:
                        self.interval[i][1]=self.interval[i+1][1]
                        self.interval.pop(i+1)
                        break
                    else:
                        self.interval[i][1]=value
                        break
                elif i == len(self.interval)-1:
                    self.interval.append([value,value])
                    self.interval = sorted(self.interval)
        return self.arr


    def getIntervals(self) -> List[List[int]]:
        return self.interval


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()