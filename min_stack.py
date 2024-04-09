# https://leetcode.com/problems/min-stack/?envType=study-plan-v2&envId=top-interview-150
class MinStack:

    def __init__(self):
        self.min_stack = []

    def push(self, val: int) -> None:
        if len(self.min_stack) == 0:
            self.min_stack.append([val, val])
            return
        min_element = self.min_stack[-1][1]
        self.min_stack.append([val, min(val, min_element)])

    def pop(self) -> None:
        self.min_stack.pop()

    def top(self) -> int:
        return self.min_stack[-1][0]

    def getMin(self) -> int:
        return self.min_stack[-1][1]

