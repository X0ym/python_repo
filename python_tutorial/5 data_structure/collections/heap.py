import heapq
from heapq import *

"""

python heap 只有最小堆 

如何使用最大堆？
    元素均为正数时，存储元素时取反，最小元素就是最大元素的负数。

操作
1. heapq.heappush(heap, item)：将 item 的值加入 heap 中，保持堆的不变性。
2. heapq.heappop(heap)：弹出并返回 heap 的最小的元素，保持堆的不变性。如果堆为空，
    抛出 IndexError 。使用 heap[0] ，可以只访问最小的元素而不弹出它。
3. heapq.heapify(x)：将list x 转换成堆，原地，线性时间内。
4. heap[0] 访问首元素



"""


def heapTest():
    # 创建堆
    h = []
    # push
    heappush(h, 10)
    heappush(h, 12)
    heappush(h, 14)
    print(h)  # [10, 12, 14]
    # pop
    heappop(h)
    print(h)  # [12, 14]

    # 堆化 原地，线性时间
    l = [1, 3, 2, 5, 0]
    heapify(l)
    print(l)  # [0, 1, 2, 5, 3]


if __name__ == '__main__':
    heapTest()
