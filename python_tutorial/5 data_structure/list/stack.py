"""
list 模拟 stack

- append：栈顶入栈
- pop()：栈顶出栈

"""

stk = [1, 2, 4]
stk.pop()

stk.append(5)
stk.append(6)
print(stk)  # [1, 2, 5, 6]

stk.pop()
print(stk)  # [1, 2, 5]
