class Stack:
    def __init__(self):
        # Using the underscore name to signal that this should be private
        self._storage = []
    def __len__(self):
        return len(self._storage)

    def push(self, item):
        self._storage.append(item)

    def pop(self):
        try:
            item = self._storage.pop()
        except IndexError:
            item = None
        return item
