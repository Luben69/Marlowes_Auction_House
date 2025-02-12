class reverse_iter:
    def __init__(self, obj):
        self.data = obj
        self.end = len(self.data)

    def __iter__(self):
        return self

    def __next__(self):
        self.end -= 1
        if self.end >= 0:
            return self.data[self.end]
        raise StopIteration
