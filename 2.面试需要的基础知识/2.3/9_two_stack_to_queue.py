class Solution:
    def __init__(self):
        self.stack_1 = []
        self.stack_2 = []

    def push(self, node):
        self.stack_1.append(node)

    def pop(self):
        # if stack_2 is not empty
        if self.stack_2:
            return self.stack_2.pop()
        elif not self.stack_1:
            return None
        else:
            # if stack_1 is not empty
            while self.stack_1:
                self.stack_2.append(self.stack_1.pop())
            return self.stack_2.pop()
