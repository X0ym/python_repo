"""
defaultdict
返回一个新的类似字典的对象。
defaultdict 是内置 dict 类的子类。 它重写了一个方法并添加了一个可写的实例变量。
其余的功能与 dict 类相同。

本对象包含一个名为 default_factory 的属性，构造时，第一个参数用于为该属性提供初始值，
默认为 None。所有其他参数（包括关键字参数）都相当于传递给 dict 的构造函数。

defaultdict 对象除了支持标准 dict 的操作，还支持以下方法作为扩展：

"""
from collections import defaultdict


def key_list_dict():
    # 使用 list 作为 default_factory
    """
        当每个键第一次遇见时，它还没有在字典里面，所以自动创建该条目，即调用 default_factory 方法，返回一个空的 list。
        list.append() 操作添加值到这个新的列表里。当再次存取该键时，就正常操作。
    """
    s = [('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
    d = defaultdict(list)
    for k, v in s:
        d[k].append(v)
    print(d)


if __name__ == '__main__':
    key_list_dict()
