class HashTable:
    def __init__(self, cap):
        self.buckets = [[] for _ in range(cap)]
        self.cap = cap

    def add(self, key, val):
        b = self.hash(key)
        for entry in self.buckets[b]:
            if entry[0] == key:
                entry[1] = val
                return
        self.buckets[b].append([key, val])

    def get(self, key):
        b = self.hash(key)
        for entry in self.buckets[b]:
            if entry[0] == key:
                return entry[1]
        return None

    def delete(self, key):
        b = self.hash(key)
        for i in range(len(self.buckets[b])):
            if self.buckets[b][i][0] == key:
                self.buckets[b][i] = self.buckets[b][-1]
                self.buckets[b].pop()
                return

    def increase_cap(self):
        old_buckets = self.buckets
        self.buckets = [[] for _ in range(self.cap * 2)]
        self.cap *= 2
        for b in old_buckets:
            for entry in b:
                self.add(entry[0], entry[1])

    def hash(self, key):
        if type(key) is int:
            return key % self.cap
        elif type(key) is str:
            h = 0
            for c in key:
                h += ord(c)
            return h % self.cap
        return None