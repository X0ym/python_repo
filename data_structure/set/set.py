"""
set
    无序无索引的集合

初始化
    s = {"a", "b}
    s = set()
    s1 = s2.copy()


1 访问元素
    无法通过索引访问 set 中的元素

1) for
2) in 使用 in 检查关键字是否存在指定值

2 set 无法修改已添加的元素

3 添加元素
- set.add(element) 添加一个元素
- set.update(set) 添加另一个集合

4 删除元素
- pop() 删除最后一个元素，但因为 set 是无序的，无法知道删除是什么元素，返回被删除的元素
- remove(item) 从 set 删除指定元素，如果不存在，将发生错误，而 discard 不会
- discard(item)

- clear() 清空 set

"""
