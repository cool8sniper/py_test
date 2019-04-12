
class Stack(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, elem):
        self.items.append(elem)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)
