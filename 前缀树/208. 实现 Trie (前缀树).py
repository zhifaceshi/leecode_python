import itertools
import collections
import math
import re
import sys
from typing import List
import functools

MAXINF = float('inf')
MININF = -float('inf')


def read_int_lst():
    return list(map(int, input().split()))


def build_3dmatrix(a, b, c, val=0):
    data = []
    for i in range(a):
        tt = []
        for j in range(b):
            t = []
            for k in range(c):
                t.append(val)
            tt.append(t)
        data.append(tt)
    return data


def build_2d_matrix(a, b, val=0):
    data = []
    for i in range(a):
        t = []
        for j in range(b):
            t.append(val)
        data.append(t)
    return data


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        p = self.root
        for w in word:
            if w not in p:
                p[w] = {}
            p = p[w]
        p['#'] = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        ans = self.find(word)
        return ans != None and '#'  in ans

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        ans = self.find(prefix)
        return ans != None

    def find(self, word):
        p = self.root
        for w in word:
            if w not in p:
                return None
            p = p[w]
        return p


