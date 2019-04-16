
# 由于链表的功能是依靠节点来完成的，所以链表的建立必然要先建立节点类。
# 我们通过节点间传递值的方式将指针指向下一个节点。
# 如下代码是一个链表的创建，下一节将介绍如何遍历(traverse)链表。


class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def show(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def append(self, node):
        node = Node(node)
        if self.head is None:
            self.head = node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = node

    def add_left(self, value):
        node = Node(value)
        self.head, self.head.next = node, self.head


li = LinkedList()
li.append("Mon")
e2 = Node("Tue")
e3 = Node("Wed")
e4 = Node("Fir")
li.head.next = e2
e2.next = e3
li.append("Fir")

li.show()
