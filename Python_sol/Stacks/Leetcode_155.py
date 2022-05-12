class MinStack:
    
    def __init__(self):
        self.stack = []
        self.cur_min = float(inf)
    
    # Add the value on the top update the min if necessary O(1)
    def push(self, val: int) -> None:
        self.stack.append(val)
        if val < self.cur_min:
            self.cur_min = val
    
    # Pop the top and update the min
    # Pop: O(1) & under the hood O(n) min update
    def pop(self) -> None:
        to_pop = self.stack.pop()
        if to_pop == self.cur_min:
            try:
                self.cur_min = min(self.stack)
            except ValueError:
                self.cur_min = float(inf)

        return to_pop
    
    # O(1)
    def top(self) -> int:
        return self.stack[-1]
    
    # O(1)
    def getMin(self) -> int:
        return self.cur_min