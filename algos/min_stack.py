class MinStack:

    def __init__(self):
        self.stack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        

    def pop(self) -> None:
        return self.stack.pop()
        

    def top(self) -> int:
        if len(self.stack) > 0:
            return self.stack[-1]
        else:
            return []
        

    def getMin(self) -> int:
        if len(self.stack) > 0:
            return min(self.stack)
        else:
            return []

if __name__ == "__main__":
    obj = MinStack()
    obj.push(9)
    obj.pop()
    param_3 = obj.top()
    param_4 = obj.getMin()
    print(param_3)
    print(param_4)