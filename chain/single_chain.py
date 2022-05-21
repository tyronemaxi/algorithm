# 单链表
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SingleChain:
    """
    单链表的实现
    """

    def __init__(self):
        self._head = None

    def add(self, data):
        """
        链表头添加元素
        :param data:
        :return:
        """
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            node.next = self._head
            self._head = node

    def append(self, data):
        """
        链表尾部添加元素
        :param data:
        :return:
        """
        node = Node(data)
        if self._head is None:
            self._head = node
        else:
            cur = self._head
            while cur.next is not None:
                cur = cur.next
            cur.next = node

    def insert(self, index, data):
        """
        插入链表指定位置, index 分为三种情况：负数，位于 0-len(listNode), 大于链表长度
        :param data:
        :return:
        """
        cur, pre = None, None
        if index <= 0:
            self.add(data)
        elif index > self.__len__():
            self.append(data)
        else:
            count = 0
            node = Node(data)
            cur = self._head
            while count < index:
                pre = cur
                cur = cur.next
                count += 1

            pre.next = node
            node.next = cur

    def find(self, data):
        """
        找到第一个链表中的数据
        :param data:
        :return: index
        """
        if self._head is None:
            return False

        cur = self._head
        index = 0
        while cur is not None:
            if cur.data == data:
                return index

            index += 1
            cur = cur.next

        return False

    def remove(self, data):
        cur = self._head
        if cur is None:
            return

        pre = None
        while cur is not None:
            if cur.data == data:
                pre.next = cur.next
            pre = cur
            cur = cur.next

    def travel(self):
        cur = self._head
        while cur is not None:
            print("-**{}".format(cur.data), end='')
            cur = cur.next
        print()

    def get_head(self):
        return self._head

    def __len__(self):
        count = 0
        cur = self._head
        while cur is not None:
            count += 1
            cur = cur.next
        return count
