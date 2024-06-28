"""

字典

1 初始化
- dict() 创建空 dict
- d = {} 创建空 dict
- d2 = d1.copy()

修改元素值
m["key"] = new_value

插入元素
dict["key"] = value
dictionary.update(iterable) 使用另一个字典对象或可迭代的键/值对 中的元素更新字典
dictionary.setdefault(keyname, value)

删除元素
pop("key")
del m["key"]

判断 key 是否存在：in


"""


def init():
    m = {
        "key1": "value1",
        "key2": 2
    }

    print(m.get("key2"))
    print(m["key1"])

    for x in m:
        print("key=%s" % x, end=" ")
    print()

    for x in m.items():
        print(x, end=" ")
    print()

    for key, val in m.items():
        print("key=%s value=%s" % (key, val))
    print()

    for key, val in enumerate(m):
        print("key=%s value=%s" % (key, val))
    print()


def del_elem():
    m = {
        "key1": "value1",
        "key2": 2
    }

    del m["key1"]
    m.pop("key2")
    print(m)


def update_elem():
    m = {
        "key1": "value1",
        "key2": 2
    }
    print(m)
    m["k"] = 2
    m.update({"key3": "apple"})  # 插入键值对
    m.update({"key3": "apple2"})  # 插入键值对
    m.update(a="for", b='geeks')  # update the Dictionary with iterable
    print(m)


if __name__ == '__main__':
    init()
    # del_elem()
    update_elem()
