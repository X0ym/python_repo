"""

list

操作

1 初始化
- 空 list arr = []
- 指定容量并赋初值 arr = [0] * size
- list 构造函数
- 复制 list

2 添加元素

- append()


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

- pop(pos) 参数 pos 可选。数字，指定需删除元素的位置。默认值 -1，返回最后的项目
- remove(element) 必需。需删除的任何类型（字符串、数字、列表等）的元素

6 list 的一些内置方法

- clear
    list.clear() 删除所有元素
- count 返回具有指定值的元素个数
    list.count(value)
    参数 value 必需
- index 返回具有指定值的第一个元素的索引
    list.index(element)
    参数 element 必需
- reverse 反转
- sort() 排序
    list.sort(reverse=True|False, key=myFunc)
    - reverse 可选。reverse=True 将对列表进行降序排序，默认是 reverse=False
    - key 可选。指定排序标准的函数

"""


def init_list():
    arr1 = []
    arr2 = [0] * 5
    arr3 = list(("a", "b", "c"))
    arr4 = list(arr3)
    arr5 = arr3.copy()

    print(arr1, arr2, arr3, arr4)


def add():
    arr = []
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
