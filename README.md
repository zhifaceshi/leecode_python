# 刷题记录（个人）  
不知道什么时候就放弃更新了，所以就不写什么长篇大论了。省的浪费时间。  
+ 来源：  
    + leetcode   
    + 牛客网   
    + ……
+ 参考：  
    + leetcode官方题解
    + 花花酱leetcode
    + ……
    

## 图

| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [886. 可能的二分法](https://leetcode-cn.com/problems/possible-bipartition/) | 中等 | 1、for i in range(1 开始, ) **2、建立双向映射（题目是无向图），而非单向（这是有向图的解法） for (x, y) in dislikes: graph[x].add(y)\n  graph[y].add(x)** ; |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 二分搜索
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [33. 搜索旋转排序数组](https://leetcode-cn.com/problems/search-in-rotated-sorted-array/submissions/) | 中等 | 各种细节bug，需要足够仔细 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 动态规划
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [790. 多米诺和托米诺平铺](https://leetcode-cn.com/problems/domino-and-tromino-tiling/submissions/) | 中等 | 想不出转移方程 |
| [53. 最大子序和](https://leetcode-cn.com/problems/maximum-subarray/) | 中等 | 最大值可能会出现在中间的状态里。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 前缀树
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 并查集

| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| 短文本 | 中等文本 | 稍微长一点的文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 树
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [109. 有序链表转换二叉搜索树](https://leetcode-cn.com/problems/convert-sorted-list-to-binary-search-tree/) | 中等 | 马虎：写了两次root.left =  |
| [222. 完全二叉树的节点个数](https://leetcode-cn.com/problems/count-complete-tree-nodes/) | 中等 | 一次AC |
| [988. 从叶结点开始的最小字符串](https://leetcode-cn.com/problems/smallest-string-starting-from-leaf/) | 中等 | 注意是叶子节点，且注意最后要额外添加叶子节点的值（类似要不要先将状态放入visited的问题） |

## 递归搜索
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [1079. 活字印刷](https://leetcode-cn.com/problems/letter-tile-possibilities/) | 中等 | 不同于全排列，这里是有字数限制的排列，维护一个字典便可以 |
| [1043. 分隔数组以得到最大和](https://leetcode-cn.com/problems/partition-array-for-maximum-sum/) | 中等 | 记忆化递归解决，但是很慢，但空间消耗较小，击败100%。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 链表
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [142. 环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii/) | 中等 | 马虎：没有能够正确返回ListNode类型。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 滑动窗口及双指针
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [187. 重复的DNA序列](https://leetcode-cn.com/problems/repeated-dna-sequences/) | 中等 | 一次AC |
| [16. 最接近的三数之和](https://leetcode-cn.com/problems/3sum-closest/) | 中等 | **不要if value:** 这种形式来判断值是不是None，因为很容易将0 误判！！！ |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 广度优先搜索
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/) | 中等 | 建dct忘记使用函数 |
| [1091. 二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/submissions/) | 中等 | 一次AC |
| 稍微长一点的文本 | 短文本 | 中等文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 数学及简单矩阵
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [807. 保持城市天际线](https://leetcode-cn.com/problems/max-increase-to-keep-city-skyline/) | 中等 | 一次AC |
| [899. 有序队列](https://leetcode-cn.com/problems/orderly-queue/) | 困难 | k = 2时可以证明可以任意交换两个相邻的字符，这样就可以冒泡排序，继而证明 k = 2 的结果一定是有序的 |
| [382. 链表随机节点](https://leetcode-cn.com/problems/linked-list-random-node/comments/) | 中等 |每个元素都有k/x的概率被选中，然后等概率的（1/k）替换掉被选中的元素。其中x是元素的序号。   [数学证明](http://sofasofa.io/forum_main_post.php?postid=1002998) |
| [554. 砖墙](https://leetcode-cn.com/problems/brick-wall/)| 中等 | 记录缝隙的位置。special test case 是[[1], [1], [1]],这个时候只能穿过三个，返回3 |
| [869. 重新排序得到 2 的幂](https://leetcode-cn.com/problems/reordered-power-of-2/) | 中等 | [计数，反过来想有多少可能的解，用hash表](https://leetcode-cn.com/problems/reordered-power-of-2/solution/zhong-xin-pai-xu-de-dao-2-de-mi-by-leetcode/) |
| [789. 逃脱阻碍者](https://leetcode-cn.com/problems/escape-the-ghosts/) | 中等 | 马虎：应该取min，结果取了max |
| [926. 将字符串翻转到单调递增](https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/) | 中等 | [前缀和解法](https://leetcode-cn.com/problems/flip-string-to-monotone-increasing/solution/jiang-zi-fu-chuan-fan-zhuan-dao-dan-diao-di-zeng-b/) |
| [372. 超级次方](https://leetcode-cn.com/problems/super-pow/) | 中等 | [快速幂](https://leetcode-cn.com/problems/super-pow/solution/python3di-gui-by-yee-8-2/)    (a*b)%c = ((a%c)*(b%c)%c |
| [1016. 子串能表示从 1 到 N 数字的二进制串](https://leetcode-cn.com/problems/binary-string-with-substrings-representing-1-to-n/) | 中等 | 遍历1到N，然后判断bin(s)[2:]是否出现在S中 |
| [458. 可怜的小猪](https://leetcode-cn.com/problems/poor-pigs/) | 中等 | 知道base 是 要 + 1的，因为已知肯定会有一个毒药桶。然后知道2只小猪，15分钟后死去，60分钟用来判断，一共可以cover 25个桶。[详细见此](https://leetcode-cn.com/problems/poor-pigs/solution/hua-jie-suan-fa-458-ke-lian-de-xiao-zhu-by-guanpen/) |
| 稍微长一点的文本 | 短文本 | 中等文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 贪心
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [455.分发饼干](https://leetcode-cn.com/problems/assign-cookies/submissions/) | 简单 | 一次AC |
| [670. 最大交换](https://leetcode-cn.com/problems/maximum-swap/) | 中等 |存储数字出现的最后一次下标，然后重新遍历，进行第一次替换。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 自定义数据结构
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [146. LRU缓存机制](https://leetcode-cn.com/problems/lru-cache/) | 中等 | [labuladong题解](https://leetcode-cn.com/problems/lru-cache/solution/lru-ce-lue-xiang-jie-he-shi-xian-by-labuladong/) 学会了哈希双向链表 ，注意self.cache.popitem **(last=False)** OrderedDict的使用要注意，pop的是最开始的值。|
| [670. 最大交换](https://leetcode-cn.com/problems/maximum-swap/) | 中等 |存储数字出现的最后一次下标，然后重新遍历，进行第一次替换。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 队列和栈
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [56. 合并区间](https://leetcode-cn.com/problems/merge-intervals/) | 中等 | 别忘了[[1,4],[2,3]] 这种内部嵌套的测试用例 |
| 稍微长一点的文本 | 短文本 | 中等文本 |


## 其他类型
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [792. 匹配子序列的单词数](https://leetcode-cn.com/problems/number-of-matching-subsequences/) | 中等 | S.index()来作查找，速度会变快很多~！用指针移动匹配的方法，会超时，但是使用S.index()，速度就很溜！！！ |
| [857. 雇佣 K 名工人的最低成本](https://leetcode-cn.com/problems/minimum-cost-to-hire-k-workers/) | 中等 | 先对工资比进行排序，然后维护一个**大根堆**来保持k个最小值的quality。 |
| [717. 1比特与2比特字符](https://leetcode-cn.com/problems/1-bit-and-2-bit-characters/) | 中等 | 跳格子的问题 |
| [1094. 拼车](https://leetcode-cn.com/problems/car-pooling/) | 中等 | 原本以为是合并区间，结果是桶排序…… |
| [674. 最长连续递增序列](https://leetcode-cn.com/problems/longest-continuous-increasing-subsequence/) | 简单 | 1、空输入特殊处理 2、return 之前还要做一次max处理，因为你count = max这一步，是假定原数组中存在降序对。如果没有降序对，这个判断就不会被触发，故需要我们在return之前再做一次~ |
| 稍微长一点的文本 | 短文本 | 中等文本 |
| 稍微长一点的文本 | 短文本 | 中等文本 |


---
# 没有解出的题
+ 1020.飞地的数量 深搜超时， 38/58
+ 1043.分隔数组以得到最大和 记忆化递归超时 14 / 52 个通过测试用例
    + 原因是求最大值的时候，要重复计算，这很低效，可以优化。(已通过，使用记忆化递归)