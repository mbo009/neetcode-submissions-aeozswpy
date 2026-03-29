class MinStack:

    def __init__(self):
        self.stack = []
        self.ordered_stack = []
        self.current_min = float('inf')

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.current_min = min(self.current_min, val)
        self.ordered_stack.append(self.current_min)
        print("push", self.stack, self.ordered_stack, self.current_min)

    def pop(self) -> None:
        del self.stack[-1]
        del self.ordered_stack[-1]
        if len(self.stack) > 0:
            self.current_min = self.ordered_stack[-1]
        else:
            self.current_min = float('inf')
        print("pop", self.stack, self.ordered_stack, self.current_min)

    def top(self) -> int:
        print("top", self.stack[-1])
        return self.stack[-1]
    def getMin(self) -> int:
        print("getMin", self.ordered_stack[-1])
        return self.ordered_stack[-1]
