"""
循环队列实现
循环队列实现可以基于取余来计算

"""


class CircleQueue(object):
    def __init__(self, n):
        self.cap = n + 1
        self._queue = [None] * self.cap
        self.head = 0
        self.tail = 0

    def enqueue(self, data):
        # 判断是否为 full
        if self.is_full():
            return False
        self._queue[self.tail] = data
        self.tail = (self.tail + 1) % self.cap
        return True

    def dequeue(self):
        if self.is_empty():
            return False
        data = self._queue[self.head]
        self._queue[self.head] = None
        self.head = (self.head + 1) % self.cap
        return data

    def head(self):
        if self.is_empty():
            return False
        data = self._queue[self.head]

        return data

    def tail(self):
        if self.is_empty():
            return False
        data = self._queue[self.tail]
        return data

    def is_full(self):
        return self.head == (self.tail + 1) % self.cap

    def is_empty(self):
        return self.head == self.tail

    def get_queue(self):
        return self._queue


if __name__ == '__main__':
    cq = CircleQueue(5)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)
    cq.enqueue(5)
    print(cq.get_queue())

    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()
    cq.dequeue()

    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)
    cq.enqueue(4)

    print(cq.get_queue())

    cq.dequeue()
    print(cq.get_queue())

