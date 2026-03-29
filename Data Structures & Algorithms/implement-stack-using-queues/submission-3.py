class MyStack:

    def __init__(self):
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        print("push ", self.stack)


    def pop(self) -> int:
        popped = self.stack[-1]
        del self.stack[-1]
        print("pop ", self.stack)
        return popped


    def top(self) -> int:
        print("top ", self.stack)
        return self.stack[-1]

    def empty(self) -> bool:
        print("empty ", self.stack)
        return len(self.stack) == 0


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()