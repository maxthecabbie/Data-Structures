class Heap:
    def __init__(self):
        self.heap = [0] * 100
        self.size = 0

    def increase_cap(self):
        self.heap += [0] * len(self.heap)

    def push(self, item):
        if self.size == len(self.heap):
            self.increase_cap()
        self.heap[self.size] = item
        self.size += 1
        self.perc_up()

    def pop(self):
        if self.size > 0:
            item = self.heap[0]
            last = self.heap[self.size - 1]
            self.heap[0] = last
            self.size -= 1
            self.perc_down()
            return item
        return None

    def peek(self):
        if self.size > 0:
            return self.heap[0]
        return None

    def perc_up(self):
        curr = self.size - 1
        par = (curr - 1)//2

        while self.heap[curr] < self.heap[par]:
            self.heap[curr], self.heap[par] = self.heap[par], self.heap[curr]
            curr = par
            par = (par - 1)//2

    def perc_down(self):
        curr = 0
        l, r = curr * 2 + 1, curr * 2 + 2

        while (self.heap[curr] > self.heap[l] or self.heap[curr] > self.heap[r]) and l < self.size:
            child = l if self.heap[l] < self.heap[r] else r
            self.heap[curr], self.heap[child] = self.heap[child], self.heap[curr]
            curr = child
            l, r = curr * 2 + 1, curr * 2 + 2

