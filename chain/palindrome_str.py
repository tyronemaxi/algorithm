"""
回文字符串判断
1. 使用快慢指针找到链表中间层
2. reverse the middle chain
3. 遍历比较

总结：
1. 字符串奇偶问题：如果是偶数，利用快慢指针遍历的退出条件：fast and fast.next, 会多遍历一次，使得慢指针在中间位置。
奇数时，会在最后一个位置
2. 反转链表。理解 rev --> p, rev.next = rev
"""
from chain.single_chain import SingleChain


def find_mid_node(head):
    fast, slow = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    return slow


def reverse_chain(head):
    rev, p = None, head

    while p:
        rev, rev.next, p = p, rev, p.next

    return rev


def judge_if_palindrome(head):
    mid = reverse_chain(find_mid_node(head))

    while mid:
        if mid.data != head.data:
            return False
        mid = mid.next
        head = head.next
    return True


if __name__ == '__main__':
    # 存储回文字符串
    my_str = '123321'
    my_str_2 = '1234321'

    c1 = SingleChain()
    for value in my_str_2:
        c1.append(value)

    head = c1.get_head()

    print(judge_if_palindrome(head))
