"""

deque
    双端队列

操作

- append(x)：队尾入队
- appendleft(x)：队首入队
- pop()：队尾出队，移去 deque 最右侧的一个元素并且返回，没有元素，引发 IndexError
- popleft()：队首出队，移去 deque 最左侧的一个元素并且返回，没有元素，引发 IndexError

count(x) 计算 deque 中 x 的个数

成员检测 in
首个元素 q[0]
队尾元素 q[len(q) - 1]

其他操作
- clear()：移除所有元素，使其长度为0
- extend(iterable)：扩展deque的右侧，通过添加iterable参数中的元素

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
