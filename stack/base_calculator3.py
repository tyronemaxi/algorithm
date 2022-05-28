"""
基本运算器 3： (1+1/2)+(123+1)*2
解题思路：
使用双栈法：stack_num 存储数字，stack_opt 存储运算符，设置运算符优先级
"""
from stack.base_stack import Stack


# 基本运算
def basic_cal(A, B, opt):
    if opt == "+":
        return int(A) + int(B)
    elif opt == '-':
        return int(B) - int(A)
    elif opt == '*':
        return int(B) * int(A)
    elif opt == '/':
        return int(B) / int(A)
    else:
        raise Exception('wrong calculated opt: {}'.format(opt))


# 优先级计算
def priority_cal(stack_opt: Stack, stack_num: Stack):
    opt = stack_opt.pull()
    A = stack_num.pull()
    B = stack_num.pull()
    num = basic_cal(A, B, opt)
    stack_num.push(num)


# 整体计算
def whole_cal(s: str) -> int:
    priority_opt = {
        "(": 0,
        ")": 0,
        "-": 1,
        "+": 1,
        "*": 2,
        "/": 2
    }

    n = len(s)
    i = 0
    stack_opt = Stack()
    stack_num = Stack()

    while i < n:
        if i == " ":
            i += 1
            continue

        if s[i].isdigit():
            start = i
            while i + 1 < n and s[i + 1].isdigit():
                i = i + 1
            num = s[start: i + 1]
            stack_num.push(num)

        elif s[i] == "(":
            stack_opt.push(s[i])

        elif s[i] == ")":
            while stack_opt.top() != "(":
                priority_cal(stack_opt, stack_num)
            stack_opt.pull()

        else:
            while not stack_opt.is_empty() and priority_opt[stack_opt.top()] >= priority_opt[s[i]]:
                priority_cal(stack_opt, stack_num)
            stack_opt.push(s[i])

        i += 1
    # 全部计算
    while not stack_opt.is_empty():
        priority_cal(stack_opt, stack_num)
    return int(stack_num.top())


if __name__ == '__main__':
    s = "((1+1-1*2)*2)+(1+2+1/1)*2"
    print(whole_cal(s))
    print(whole_cal("(1=2)"))
