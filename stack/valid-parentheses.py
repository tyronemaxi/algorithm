'''
链接：https://leetcode.cn/problems/valid-parentheses/
'''

from stack.base_stack import Stack

def is_valid(s: str):
    # 括号是成对出现的
    n = len(s)
    if n % 2 == 1:
        return False

    stack = Stack()
    rules = {
        ")": "(",
        "}": "{",
        "]": "["
    }

    for ch in s:
        if ch in rules:
            if not stack or stack.top() != rules[ch]:
                return False
            stack.pull()
        else:
            stack.push(ch)
    return stack.is_empty()


if __name__ == '__main__':
    print(is_valid('{}'))
    print(is_valid('{()}'))
    print(is_valid('({{[]}})'))
    print(is_valid('({{[()]}})'))
    print(is_valid('({{[}{]}})'))
