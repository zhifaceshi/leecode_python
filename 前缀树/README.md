# 前缀树模板

```python
class Trie():
    def __init__(self):
        self.root = {}

    def insert(self, word):
        p = self.root
        for w in word:
            if w not in p:
                p[w] = {}
            p = p[w]

        p['#'] = True

    def search(self, word):
        root = self.find(word)
        if root is not None and '#' in root:
            return True
        return False

    def startsWith(self, prefix: str) -> bool:
        return self.find(prefix) is not None

    def find(self, word):
        p = self.root
        for w in word:
            if w not in p:
                return None
            p = p[w]
        return p
```

+ 根据这个模板，可以有很多的变形题。
+ 题很多也与树的遍历有关，递归or层次

|题目|改造点|   
|---|---|  
|421. 数组中两个数的最大异或值|遍历|  
