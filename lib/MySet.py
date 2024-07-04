class MySet:
    def __init__(self, elements=None):
        self.dictionary = {}
        if elements is not None:
            for element in elements:
                self.dictionary[element] = True  # Use dictionary keys to simulate set behavior.

    def add(self, element):
        self.dictionary[element] = True

    def delete(self, element):
        if element in self.dictionary:
            del self.dictionary[element]

    def has(self, element):
        return element in self.dictionary

    def size(self):
        return len(self.dictionary)

    def clear(self):
        self.dictionary.clear()

    def __str__(self):
        return f'MySet: {{{",".join(map(str, self.dictionary.keys()))}}}'
