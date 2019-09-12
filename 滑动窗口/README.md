# 滑动窗口模板题

参考 [滑动窗口算法通用思想](https://leetcode-cn.com/problems/minimum-window-substring/solution/hua-dong-chuang-kou-suan-fa-tong-yong-si-xiang-by-/)里提出的模板  
以 [76. 最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring/)为例
```python
s = "ADOBECODEBANC"
t = "ABC"
# 期望输出"BANC"
# 起初l 与 r 要重叠
l = 0
r = 0
window = []
res = 1e14
while r < len(s):
    # 先添加到窗口中
    window.append(s[r])
    # r指针右移
    r += 1
    # 如果window满足条件
    while f(window):
    # 更新答案
        res = min(res, len(window))
        # 窗口弹出值，并且指针右移
        # 因为有while 循环，会一直移动到不满足条件为止
        window.pop(0)
        l += 1
```

---
最简单的滑动窗口是固定大小的窗口，真·滑动窗口。
```
winsize = 10
for i in range(len(s) - winsize + 1):
    j = i + winsize
```
注意：for 循环里 i 的范围是 len(s) - winsize + 1  
其次，j = i + winsize 表示开区间，左闭右开，一般用于字符串截取

---

