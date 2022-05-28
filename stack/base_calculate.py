"""
基本运算器实现
不具备括号，类似 1+1*2/3
"""
from stack.base_stack import Stack


def calculate(s):
    n = len(s)
    _stack = []
    num = 0
    pre_sign = '+'
    for i in range(n):
        if s[i] != ' ' and s[i].isdigit():
            num = num * 10 + ord(s[i]) - ord('0')

        if i == n - 1 or s[i] in '+-*/':
            if pre_sign == '+':
                _stack.append(num)
            if pre_sign == '-':
                _stack.append(-num)
            if pre_sign == '*':
                _stack.append(int(_stack.pop() * num))
            else:
                _stack.append(int(_stack.pop() / num))
            pre_sign = s[i]
            num = 0

    return sum(_stack)


if __name__ == '__main__':
    my_str = '1+1/1*2+1+1+2/2'
    print(calculate(my_str))
