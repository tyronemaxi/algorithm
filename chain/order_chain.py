from chain.double_direction_chain import DoubleLink
from chain.double_direction_chain import XNode


# 有序双向链表，记录上一次的查找的 pos, 决定向前还是向后查找
class OrderLink(DoubleLink):
    def __init__(self):
        super(DoubleLink, self).__init__()
        self._head = None
        self._pos = None
        self._find_node = None

    def add(self, data):
        node = XNode(data)
        # status 1: 链表为空
        if self._head is None:
            self._head = node
            return

        # status 2: 链表只有一个节点
        if self._head.next is None:
            # 插入数据大于该节点, 直接在尾部插入
            if self._head.data <= data:
                node.prev = self._head
                self._head.next = node
                return

            else:
                # 否则直接在首部插入
                node.next = self._head
                self._head.prev = node
                self._head = node
                return

        # status 3: 链表有多个节点
        else:
            cur = self._head
            tail = self.tail()
            if data >= tail.data:
                # 尾部加入
                tail.next = node
                node.prev = tail
                return

            while cur.next is not None and data > self._head.data:
                # 找到对应节点
                cur = cur.next

            if cur == self._head:
                # 首部插入
                node.next = self._head
                self._head.prev = node
                self._head = node
                return

            node.next = cur
            node.prev = cur.prev
            cur.prev.next = node
            cur.prev = node
            return

    def find(self, data):
        cur = self._head
        if cur is None:
            return
        if self._find_node:
            _cur = self._find_node
            if data >= self._find_node.data:
                # 向后查找
                pos = self._pos
                while _cur is not None:
                    if data == _cur.data:
                        self._pos = pos
                        self._find_node = _cur
                        return pos
                    _cur = _cur.next
                    pos += 1
            else:
                # 向前查找
                pos = self._pos
                while _cur is not None:
                    if data == _cur.data:
                        self._pos = pos
                        self._find_node = _cur
                        return pos

                    _cur = _cur.prev
                    pos -= 1

        else:
            # 遍历查找
            pos = 0
            while cur is not None:
                if data == cur.data:
                    self._pos = pos
                    self._find_node = cur
                    return pos
                cur = cur.next
                pos += 1

    def travel(self):
        cur = self._head

        while cur.next is not None:
            print("-**{}".format(cur.data), end='')
            cur = cur.next
        print("-**{}".format(cur.data), end='')  # 由于是 cur.next 判断的，故 cur 指向最后一个节点
        print()

    def tail(self):
        cur = self._head
        while cur.next is not None:
            cur = cur.next

        return cur

    def obtain_head(self):
        return self._head
