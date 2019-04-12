

class Tree(object):

    def __init__(self, data, ltree=None, rtree=None):
        self.ltree = ltree
        self.rtree = rtree
        self.data = data


class BTree(object):

    def __init__(self, base=None):
        self.base = base

    def _empty(self):
        if self.base is None:
            return True
        return False

    def qout(self, tree_base):
        if tree_base is None:
            return
        print(tree_base.data)
        self.qout(tree_base.ltree)
        self.qout(tree_base.rtree)

    def mout(self, tree_base):
        if tree_base is None:
            return
        self.mout(tree_base.ltree)
        print(tree_base.data)
        self.mout(tree_base.rtree)

    def hout(self, tree_base):
        if tree_base is None:
            return
        self.hout(tree_base.ltree)
        self.hout(tree_base.rtree)
        print(tree_base.data)

    @staticmethod
    def level_queue(tree_base):
        if tree_base is None:
            return
        node = tree_base
        node_list = [node]
        while node_list:
            node = node_list.pop(0)
            print(node.data)
            if node.ltree:
                node_list.append(node.ltree)
            if node.rtree:
                node_list.append(node.rtree)


if __name__ == '__main__':
    #         5
    #     6         7
    # 8     None  9   None

    tree1 = Tree(data=8)
    tree2 = Tree(data=9)
    tree3 = Tree(data=6, ltree=tree1)
    tree4 = Tree(data=7, ltree=tree2)
    btree = BTree(Tree(5, tree3, tree4))
    # print('前序遍历结果: 56879')
    # btree.qout(btree.base)

    # print('中序遍历结果: 86597')
    # btree.mout(btree.base)

    # print('后序遍历结果: 86975')
    # btree.hout(btree.base)

    # print('层次遍历结果: 56789')
    # btree.level_queue(btree.base)
