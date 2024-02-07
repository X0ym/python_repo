"""

deque
    双端队列

操作

append(x)
appendleft(x)
pop()
popleft()

count(x) 计算 deque 中 x 的个数

成员检测 in
首个元素 q[0]
队尾元素 q[len(q) - 1]

"""
from collections import deque


def init():
    q = deque()
    q.append(1)
    q.appendleft(2)
    q.append(3)
    print(q)

    # 队首
    print(q[0])
    # 队尾
    print(q[len(q) - 1])


if __name__ == '__main__':
    init()
