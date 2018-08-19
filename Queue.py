class Queue():
    def __init__(self):
        self.queue = LinkedList()
        self.size = 0

    def enqueue(self, item):
        self.queue.add_back(item)
        self.size += 1

    def dequeue(self):
        self.size = max(self.size - 1, 0)
        return self.queue.remove_front()

    def empty(self):
        return self.size == 0

    def peek(self):
        return self.queue.head.val if self.queue.head else None

class CircularQueue():
    def __init__(self, cap):
        self.queue = [0] * cap
        self.cap = cap
        self.size = 0
        self.head = 0
        self.tail = 0

    def enqueue(self, item):
        if self.size == self.cap:
            return False
        self.queue[self.tail] = item
        self.tail = self.tail + 1 if self.tail + 1 < self.cap else 0
        self.size += 1
        return True

    def dequeue(self):
        if not self.empty():
            item = self.queue[self.head]
            self.head = self.head + 1 if self.head + 1 < self.cap else 0
            self.size -= 1
            return item
        return None

    def peek(self):
        return self.queue[self.head] if not self.empty() else None

    def empty(self):
        return self.size == 0