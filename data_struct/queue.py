

class Queue(object):
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, elem):
        self.items.insert(0, elem)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop()
        return

    def size(self):
        return len(self.items)
