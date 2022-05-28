# 顺序栈的实现

class Stack(object):
    def __init__(self):
        """
        :param capacity: the capacity of stack
        """
        self._stack = []

    def push(self, data):
        """
        入栈
        """
        self._stack.append(data)

    def pull(self):
        """
        出栈
        """
        if self.is_empty():
            return
        return self._stack.pop()

    def top(self):
        if self.is_empty():
            return
        return self._stack[-1]

    def size(self):
        return len(self._stack)

    def is_empty(self):
        if self._stack:
            return False
        else:
            return True

    def get_stack(self):
        return s._stack


if __name__ == '__main__':
    s = Stack()
    s.push(1)
    s.push(2)
    s.push(3)
    s.push(4)

    print(s.get_stack())

    s.pull()
    s.pull()
    print(s.get_stack())
