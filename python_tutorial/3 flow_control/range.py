"""
range 对象
    class range(stop)
    class range(start, stop[, step])
参数说明
    1. 如果省略 step 参数，则默认为 1。
    2. 如果省略 start 参数，则默认为 0。
    3. 如果 step 为零，则会引发 ValueError。
        step 为正值，确定 range r 内容的公式为 r[i] = start + step*i 其中 i >= 0 且 r[i] < stop
        step 为负值，确定 range 内容的公式仍然为 r[i] = start + step*i，但限制条件为 i >= 0 且 r[i] > stop.

"""

# [0, 3)
for i in range(3):
    print(i, end=' ')
print()  # 0 1 2

# [1, 5) 指定 start 和 stop
for i in range(1, 5):
    print(i, end=' ')
print()  # 1 2 3 4

# [1, 5) step=2
for i in range(1, 5, 2):
    print(i, end=' ')
print()  # 1 3
