"""

1) 字符串查找和统计
1. 使用 in 或 not in 判断子串是否存在
2. 指定范围查找子串
    S.find(sub[, start[, end]]) -> int
        返回子字符串 sub 在 s[start:end] 切片内被找到的最小索引。未找到返回 -1
    S.count(sub[, start[, end]]) -> int
        返回子字符串 sub 在 [start, end] 范围内非重叠出现的次数。
3. 查找前缀或后缀
    S.startswith(prefix[, start[, end]]) -> bool
    S.endswith(suffix[, start[, end]]) -> bool
4. 统计字符串中不同字符数
    str -> set
"""


# 字符串查找和统计
def str_find():
    str0 = "001122"
    print(set(str0))  # {'0', '2', '1'}

    #  使用 in 或 not in 判断子串是否存在
    s = "0123456789"
    print("12" in s)
    if "23" in s:
        print("23 is in s")

    print(s.find("34"))

    print(s.count("12"))

    print(s.startswith("012"))
    print(s.endswith("92"))


def str_op():
    s = "this is str template"
    print("s length: ", len(s))  # s length:  20

    # prefix and suffix
    if s.startswith("this"):
        print("s startswith this")
    else:
        print("s not startswith this")

    if s.endswith("str"):
        print("s endswith str")
    else:
        print("s not endswith str")


if __name__ == '__main__':
    str_op()
    str_find()
