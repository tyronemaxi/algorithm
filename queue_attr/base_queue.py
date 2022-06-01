"""
队列的实现
基于数组实现
队列长度为 n
"""


class Queue(object):
    def __init__(self, n):
        self._queue = []
        self.n = n

    def enqueue(self, data):
        """
        入队
        :param data:
        :return:
        """
        if self.size() > self.n:
            raise Exception("the queue_attr is full")
        self._queue.append(data)

    def dequeue(self):
        """
        出队
        :return:
        """
        if self.size() > 0:
            self._queue.pop(0)
        else:
            raise Exception("the queue_attr is empty")

    def size(self):
        """
        队列的长度
        :return:
        """
        return len(self._queue)

    def head(self):
        """
        队首
        :return:
        """
        return self._queue[0]

    def tail(self):
        """
        队尾
        :return:
        """
        return self._queue[-1]

    def get_queue(self):
        return self._queue


if __name__ == '__main__':
    queue = Queue(10)
    queue.enqueue(1)
    queue.enqueue(2)
    queue.enqueue(3)
    queue.enqueue(4)
    queue.enqueue(5)

    queue.dequeue()

    print(queue.head())
    print(queue.tail())

    queue.dequeue()
    queue.dequeue()
    queue.dequeue()

    print(queue.get_queue())
