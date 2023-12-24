"""

range 类型表示不可变的数字序列，通常用于在 for 循环中循环指定的次数。

    range(stop)
    range(start, stop[, step])

"""

if __name__ == '__main__':
    range(10)
    range(1, 10)
    range(1, 10, 2)

    l = list(range(10))
    print(l)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
