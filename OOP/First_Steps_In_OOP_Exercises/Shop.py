class Shop:
    def __init__(self, name: str, items: list):
        self.name = name
        self.items = items

    def get_items_count(self):
        i = 0
        for _ in self.items:
            i += 1
        return i
