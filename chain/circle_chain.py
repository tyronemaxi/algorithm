from chain.single_chain import SingleChain
from chain.single_chain import Node


# 循环链表
class CircleLink(SingleChain):
    def __init__(self):
        super(CircleLink, self).__init__()
        self._head = None

    def add(self, data):
        node = Node(data)
        if self._head is None:
            node.next = node
            self._head = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            self._head = node
            cur.next = node

    def append(self, data):
        node = Node(data)
        if self._head is None:
            node.next = self._head
            self._head = node
        else:
            cur = self._head
            while cur.next != self._head:
                cur = cur.next
            node.next = self._head
            cur.next = node

    def travel(self):
        cur = self._head
        while cur.next != self._head:
            print("-**{}".format(cur.data), end='')
            cur = cur.next
        print("-**{}".format(cur.data), end='')  # 由于是 cur.next 判断的，故 cur 指向最后一个节点
        print()

    def find(self, data):
        if self._head is None:
            return False

        cur = self._head
        index = 0
        while cur.next != self._head:
            if cur.data == data:
                return index
            index += 1
            cur = cur.next
        if cur.data == data:  # 最后一个
            return self.__len__()

        return False

    def remove(self, data):
        cur = self._head
        if cur.next == self._head:
            self._head = None
            return

        pre = None
        while cur.next != self._head:
            if cur.data == data:
                pre.next = cur.next
                return
            pre = cur
            cur = cur.next

        # 退出循环, cur指向尾结点
        if cur.data == data:
            # 链表中只有一个结点
            pre.next = self._head
            return

    def __len__(self):
        count = 0
        cur = self._head
        while cur.next != self._head:
            count += 1
            cur = cur.next
        return count + 1  # 未计算最后一个 Node
