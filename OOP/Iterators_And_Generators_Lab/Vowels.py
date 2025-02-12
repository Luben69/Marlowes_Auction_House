class vowels:
    def __init__(self, our_strings: str):
        self.our_strings = our_strings
        self.vowels = [el for el in self.our_strings if el.lower() in 'a e i o u y']
        self.letter = -1

    def __iter__(self):
        return self

    def __next__(self):
        self.letter += 1
        if self.letter < len(self.vowels):
            return self.vowels[self.letter]
        raise StopIteration
