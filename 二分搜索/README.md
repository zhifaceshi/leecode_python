# 二分搜索模板

+ l, r 左闭右开
+ f(x) 是退出条件
+ g(x) 是判断r = m 条件的函数

套用 [花花酱leetcode](https://zxi.mytechroad.com/blog/category/algorithms/binary-search/) 总结的模板

注意：区间左闭右开 [)

```python
def binary_search(l, r):
    while l < r:
        m = (l + r) // 2

        if f(m):
            return m
            
        if g(m):
            r = m
        else:
            l = m + 1
        return l
# 如果m满足某种条件，直接返回答案
def f(m):
    pass
# 判断区间移动的条件
def g(m):
    pass

```

