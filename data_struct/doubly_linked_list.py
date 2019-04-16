

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList(object):

    def __init__(self):
        self.head = None

    def push(self, value):
        node = Node(value)
        node.next = self.head
        if self.head is not None:
            self.head.prev = node
        self.head = node

    @staticmethod
    def list_print(node):
        while node is not None:
            print(node.data)
            node = node.next

    def __len__(self):
        p = self.head
        i = 0
        if p:
            i = 1
        else:
            return i
        while p.next:
            i += 1
            p = p.next
        return i

    def reverse(self):
        length = self.__len__()
        i = 0
        p = self.head.next
        while p.next:
            p = p.next
        else:
            last = p
        first = self.head.next
        while i < length:
            first.value, last.value = last.value, first.value
            first = first.next
            last = last.prev
            i += 1
            length -= 1


l1 = DoublyLinkedList()
l1.push(12)
l1.push(8)
l1.push(62)
# l1.list_print(l1.head)
print(l1.reverse())
