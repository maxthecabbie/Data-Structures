class Stack:
    def __init__(self):
        self.stack = []
        self.size = 0

    def push(self, item):
        self.stack.append(item)
        self.size += 1

    def pop(self):
        if not self.empty():
            item = self.stack.pop()
            self.size -= 1
            return item
        return None
        
    def empty(self):
        return self.size == 0

    def peek(self):
        return self.stack[-1] if not self.empty() else None

