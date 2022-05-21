from chain.single_chain import SingleChain


# 双向链表
class XNode(object):
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None


# 双向链表
class DoubleLink(SingleChain):
    def __init__(self):
        super(DoubleLink, self).__init__()
        self._head = None

    def add(self, data):
        node = XNode(data)
        if self._head is None:
            self._head = node
            return
        else:
            node.next = self._head
            self._head.prev = node
            self._head = node
            return

    def append(self, data):
        node = XNode(data)
        if self._head is None:
            self._head = node
            return
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next

            cur.next = node
            node.prev = cur
            return

    def insert(self, index, data):
        if index < 0:
            self.add(data)
            return

        elif index >= self.__len__():
            self.append(data)
            return

        else:
            # status 1: 空
            cur = self._head
            if cur is None:
                self.add(data)
                return

            # status 2: 只有一个节点
            if cur.next is None:
                if index <= 0:
                    self.add(data)
                    return
                if index >= self.__len__():
                    self.append(data)
                    return

            # status 多个节点
            else:
                count = 0
                node = XNode(data)
                cur = self._head
                while count < index:
                    cur = cur.next
                    count += 1

                node.next = cur
                node.prev = cur.prev
                cur.prev.next = node
                cur.prev = node


if __name__ == '__main__':
    list_node = DoubleLink()
    list_node.add(1)
    list_node.add(3)
    list_node.add(2)
    # list_node.add(0)
    # list_node.add(5)
    # list_node.add(4)
    # list_node.add(7)
    # list_node.add(5)
    list_node.insert(1, 79)
    list_node.insert(2, 2)
    list_node.insert(-1, -1)
    list_node.insert(100, 100)
    list_node.insert(3, 33)

    # list_node.append('哈哈')
    # list_node.append('嘻嘻')

    list_node.travel()
    #
    # print(list_node.find(5))
    # print(list_node.find(7))
    # print(list_node.find(0))

    # cur = list_node.obtain_head()
    # while cur.next != None:
    #     print(cur.data)
    #     cur = cur.next
    #
    # print(cur.prev.data)
    # while cur.prev != None:
    #     print(cur.data)
    #     cur = cur.prev
    # print(list_node.find(2))
    # # print("链表的长度为：{}".format(len(list_node)))
    # list_node.insert(-10, -10)
    # list_node.insert(100, 100)
    # list_node.insert(2, '嚯嚯')
    # list_node.travel()
    # print(list_node.find(100))
    # list_node.remove('嘻嘻')
    # list_node.remove('哈哈')
    # list_node.remove(100)
    # list_node.travel()
