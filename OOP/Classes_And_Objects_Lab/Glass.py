class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0

    def fill(self, ml):
        if ml < self.capacity:
            if ml + self.content <= self.capacity:
                self.content += ml
                return f"Glass filled with {ml} ml"
            else:
                return f"Cannot add {ml} ml"
        else:
            return f"Cannot add {ml} ml"

    def empty(self):
        self.content -= self.content
        return "Glass is now empty"

    def info(self):
        return f"{self.capacity - self.content} ml left"