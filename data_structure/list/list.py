"""

list

操作

1 初始化
- 空 list arr = []
- 指定容量并赋初值 arr = [0] * size
- list 构造函数 list() 或 list(iterable)
- 复制 list.copy()
- 用列表推导式: [x for x in iterable]

2 添加元素

- list.append()


3 获取元素

1) 根据索引获取元素
    注意：负的索引从末尾开始， -1 表示最后一个元素，-2 表示倒数第二个元素
2) arr[left:right]

3) 遍历

for in list:
    val

for i in range(len(list)):
    i list[i]

for i enumerate(list):
    list[i]

for i, x enumerate(list):


4 更新元素

5 删除元素
- pop(pos) 参数 pos 可选。数字，指定需删除元素的位置。默认值 -1。
    函数删除列表中指定位置的元素，并返回被删除的元素
- remove(x) 必需。需删除的任何类型（字符串、数字、列表等）的元素
    删除列表中第一个值为 x 的元素，未找到元素时，触发 ValueError 异常

6 list 的一些内置方法
- clear
    list.clear() 删除所有元素
- count 返回具有指定值的元素个数
    list.count(x) 返回列表中元素 x 出现的次数
    参数 value 必需
- index 返回具有指定值的第一个元素的索引
    list.index(x)，返回列表中第一个值为 x 的元素下标。
        如果元素不存在，发生 ValueError 异常。
    list.index(x[, start[, end]]) 可选参数 start 和 end 可用于指定列表的
        特定子列表
    参数 x 必需
- reverse 反转
    list.reverse() 列表元素逆序
- sort() 排序
    list.sort(reverse=True|False, key=myFunc)
    - reverse 可选。reverse=True 将对列表进行降序排序，默认是 reverse=False
    - key 可选。指定排序标准的函数

"""


def init_list():
    arr1 = []
    arr2 = [0] * 5
    arr3 = list(("a", "b", "c"))  # list('abc') : ['a','b','c']
    arr4 = list(arr3)
    arr5 = arr3.copy()

    # 列表推导式
    arr6 = []

    print(arr1, arr2, arr3, arr4, arr5)


def add():
    arr = list()
    arr.append(1)

    print(len(arr))


def get():
    arr = ["apple", "banana", "cherry"]
    print(arr[2], arr[-1], arr[-2])

    print(arr[-5:4])  # ['apple', 'banana', 'cherry']
    print(arr[-1:4])  # ['cherry']
    print(arr[1:5])  # ['banana', 'cherry']


def ite():
    arr = [1, 2, 4]
    for x in arr:
        print(x, end=" ")
    print()

    for i in range(len(arr)):
        print(arr[i], end=" ")
    print()

    # (0, 1) (1, 2) (2, 4)
    for i in enumerate(arr):
        print(i, end=" ")
    print()

    for idx, val in enumerate(arr):
        print("index=%d val=%d" % (idx, val))
    print()


if __name__ == '__main__':
    # init_list()
    # add()
    # get()
    ite()
