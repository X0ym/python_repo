"""
bool
    true false

除空字符串外，任何字符串均为 True
除 0 外，任何数字均为 True
除空列表外，任何列表、元组、集合和字典均为 True


"""

print(bool("abc"))
print(bool(12))
print(bool(["apple", "cherry", "banana"]))

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))
