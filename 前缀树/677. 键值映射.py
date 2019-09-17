

class MapSum(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}
        self.visited = set()

    def insert(self, key, val):
        """
        :type key: str
        :type val: int
        :rtype: None
        """
        if key  in self.visited:
            self.override(key, val)
        else:
            self.update(key, val)
        self.visited.add(key)

    def update(self, key, val):
        p = self.root
        for w in key:
            if w in p:
                p[w]['val'] += val
            else:
                p[w] = {'val': val, }
            p = p[w]
        p['#'] = True

    def override(self, key, val):
        p = self.root
        for w in key:

            if w in p:
                p[w]['val'] = val
            else:
                p[w] = {'val': val, }
            p = p[w]
        p['#'] = True

    def sum(self, prefix):
        """
        :type prefix: str
        :rtype: int
        """
        count = 0
        p = self.root
        for w in prefix:
            if w not in p:
                return 0
            count = p[w]['val']
            p = p[w]
        return count

a = MapSum()
a.insert('aa', 3)
print(a.sum('a'))
a.insert('ab', 2)
print(a.sum('a'))
