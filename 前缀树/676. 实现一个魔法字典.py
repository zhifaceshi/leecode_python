import itertools
import collections
import math
import re
import sys
MAXINF = float('inf')
MININF = -float('inf')

def read_int_lst():
    return list(map(int, input().split()))

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

    def startsWith(self, prefix):
        return self.find(prefix) is not None

    def find(self, word):
        p = self.root
        for w in word:
            if w not in p:
                return None
            p = p[w]
        return p

class wordSub(Trie):

    def judge(self, word):
        t = self.root
        for i, c in enumerate(word):
            if '#' in t:
                return word[: i]
            elif c not in t:
                break
            t = t[c]
        return word

##########################################################################################


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def buildDict(self, dict):
        """
        Build a dictionary through a list of words
        :type dict: List[str]
        :rtype: None
        """
        for word in dict:
            self.insert(word)

    def insert(self, word):
        p = self.root
        for w in word:
            if w not in p:
                p[w] = {}
            p = p[w]
        p['#'] = True

    def search(self, word):
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        return self.dfs(0, word, 1, self.root)

    def dfs(self,i,word, k, p):
        if k < 0:
            return False
        if not isinstance(p, type({})):
            return False
        if i >= len(word):
            if k == 0 and '#' in p:
                return True
            else:
                return False

        ans = False
        for can in p:
            if word[i] == can:
                ans = ans or self.dfs(i+1, word, k, p[can])
            else:
                ans = ans or self.dfs(i+1, word, k-1, p[can])
            if ans:
                return True
        return ans

dict = ["hello","hallo","leetcode"]
# dict = ["hello","leetcode"]
obj = MagicDictionary()
obj.buildDict(dict)
print(obj.search('hello'))
print(obj.search('hhllo'))
print(obj.search('hell'))
print(obj.search('leetcoded'))
#
# dict = ["hello", 'hallo', "leetcode"]
# obj = MagicDictionary()
# obj.buildDict(dict)
# print(obj.search('hello'))
# print(obj.search('hhllo'))
# print(obj.search('hell'))
# print(obj.search('leetcoded'))

