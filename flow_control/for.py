"""

"""

v1 = ["num1", "num2", "num3"]
for i in v1:
    print(i)
    if i == "num1":
        continue
    if i == "num2":
        break

for x in range(10):
    if x % 2:
        print(x, end=' ')
print()  # 1 3 5 7 9

for x in range(1, 5):
    print(x, end=' ')
print()  # 1 2 3 4

for x in range(2, 10, 2):
    print(x, end=' ')
print()  # 2 4 6 8

l = [1, 3, 5, 6]
for i, v in enumerate(l):
    print("i= ", i, " v= ", v)
