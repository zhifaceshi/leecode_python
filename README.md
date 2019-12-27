# 刷题记录（个人）  
不知道什么时候就放弃更新了，所以就不写什么长篇大论了。省的浪费时间。  
+ 来源：  
    + leetcode   
    + lintcode   
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
| [980. 不同路径 III](https://leetcode-cn.com/problems/unique-paths-iii/) | 中等 | 可以将过去的数据标记为另一个值，表示已经走过了，这样就省略了visited单独用于表示是否已经访问过。会节省很多事。 |
| [695. 岛屿的最大面积](https://leetcode-cn.com/problems/max-area-of-island/) | 中等 | 将岛屿的参数进行修改，和980的思路类似~此题是走过的路径置为零。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |
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
| [877. 石子游戏](https://leetcode-cn.com/problems/stone-game/) | 中等 | 字节跳动考了一道类似的改编题。解法是：[分先后手，用一个tuple来表示。这里是一个通用的博弈类的解法。](https://leetcode-cn.com/problems/stone-game/solution/jie-jue-bo-yi-wen-ti-de-dong-tai-gui-hua-tong-yong/) |
| [712. 两个字符串的最小ASCII删除和](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings/) | 中等 | 编辑距离，注意当字相等的时候，是dp[i][j] = dp[i-1][j-1] |
| [647. 回文子串](https://leetcode-cn.com/problems/palindromic-substrings/) | 中等 | 先写一个函数用于判断是否是回文字串，然后统计dp矩阵为True的个数便可。 |
| [11. 盛最多水的容器](https://leetcode-cn.com/problems/container-with-most-water/) | 中等 | 一次ac |
| [931. 下降路径最小和](https://leetcode-cn.com/problems/minimum-falling-path-sum/) | 中等 | 很普通的动态规划~ |
| [121. 买卖股票的最佳时机](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/) | 中等 | 一次ac |
| [122. 买卖股票的最佳时机 II](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-ii/) | 中等 | 一次ac |
| [123. 买卖股票的最佳时机 III](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-iii/) | 中等 | 注意要放在买入，认为是一次交易，则 dp[k][i-1][1] + prices[i-1] 表示第k次买入再卖出，因此是正确的。 |
| [309. 最佳买卖股票时机含冷冻期](https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/) | 中等 | 和上一题一样，要以买入为准，这样卖出操作才会恰好是当前的结果。 |
| [486. 预测赢家](https://leetcode-cn.com/problems/predict-the-winner/) | 中等 | 使用了记忆化递归来实现，注意后手要选择 min， 因为对方肯定会最优，留给自己的会是小的那个~！。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |


## 前缀树
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [208. 实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/) | 中等 | 最基础，必须经常刷~ |
| [676. 实现一个魔法字典](https://leetcode-cn.com/problems/implement-magic-dictionary/) | 中等 | 注意hello，与hallo。for循环遍历所有可能性在外侧，这样可以照顾到所有的可能。 |
| [677. 键值映射](https://leetcode-cn.com/problems/map-sum-pairs/) | 中等 | override与update的判断 |
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
| [654. 最大二叉树](https://leetcode-cn.com/problems/maximum-binary-tree/) | 中等 | 一次ac |
| [814. 二叉树剪枝](https://leetcode-cn.com/problems/binary-tree-pruning/) | 中等 | 一次ac |
| [94. 二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal/) | 中等 | 非递归实现 |
| [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal/) | 中等 | 非递归实现，注意区别有没有访问过右指针，让r指向访问过的最后一个节点便可 |
| [513. 找树左下角的值](https://leetcode-cn.com/problems/find-bottom-left-tree-value/) | 中等 | 使用深度优先搜索来做 |
| [1161. 最大层内元素和](https://leetcode-cn.com/problems/maximum-level-sum-of-a-binary-tree/) | 中等 | 一次oc |
| [144. 二叉树的前序遍历](https://leetcode-cn.com/problems/binary-tree-preorder-traversal/) | 中等 | stack.pop()，而不是stack.pop(0) |
| [236. 二叉树的最近公共祖先](https://leetcode-cn.com/problems/lowest-common-ancestor-of-a-binary-tree/) | 中等 | 注意递归，都没有找到，返回None |
| [515. 在每个树行中找最大值](https://leetcode-cn.com/problems/find-largest-value-in-each-tree-row/) | 中等 | BFS |
| [226. 翻转二叉树](https://leetcode-cn.com/problems/invert-binary-tree/) | 中等 | 递归与非递归实现。实际上非递归实现，也就是BFS，只是取出节点的时候，将节点左右交换便可。 |
| [101. 对称二叉树](https://leetcode-cn.com/problems/symmetric-tree/) | 中等 | 递归与非递归的实现。实际上非递归还是使用了BFS，，只是要将None考虑进去。 |
| [337. 打家劫舍 III](https://leetcode-cn.com/problems/house-robber-iii/) | 中等 | 树和动态规划的结合，注意，当不选的时候，值返回的是 max(left) + max(right)。因为无论是左侧子树还是右侧子树，我们不care它选没选，我们只关心最大值。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |


## 递归搜索
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [1079. 活字印刷](https://leetcode-cn.com/problems/letter-tile-possibilities/) | 中等 | 不同于全排列，这里是有字数限制的排列，维护一个字典便可以 |
| [1043. 分隔数组以得到最大和](https://leetcode-cn.com/problems/partition-array-for-maximum-sum/) | 中等 | 记忆化递归解决，但是很慢，但空间消耗较小，击败100%。 |
| [78. 子集](https://leetcode-cn.com/problems/subsets/) | 中等 | 一次ac |
| [241. 为运算表达式设计优先级](https://leetcode-cn.com/problems/different-ways-to-add-parentheses/) | 中等 | 一次ac |
| [216. 组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/) | 中等 | 一次ac |
| [131. 分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/) | 中等 | 一次ac |
| [638. 大礼包](https://leetcode-cn.com/problems/shopping-offers/) | 中等 | 通过优化，解决。多重背包问题，视作是0/1背包问题就会很慢。 |
| [526. 优美的排列](https://leetcode-cn.com/problems/beautiful-arrangement/) | 中等 | 一次ac |
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
| [905. 按奇偶排序数组](https://leetcode-cn.com/problems/sort-array-by-parity/)| 简单 | 双指针滑动便可，一次ac |
| 稍微长一点的文本 | 短文本 | 中等文本 |

## 广度优先搜索
| 题目 | 难度 | 易错点 |
| ------ | ------ | ------ |
| [433. 最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation/) | 中等 | 建dct忘记使用函数 |
| [1091. 二进制矩阵中的最短路径](https://leetcode-cn.com/problems/shortest-path-in-binary-matrix/submissions/) | 中等 | 一次AC |
| [841. 钥匙和房间](https://leetcode-cn.com/problems/minimum-falling-path-sum/) | 中等 | 普通的BFS |
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
| [59. 螺旋矩阵 II](https://leetcode-cn.com/problems/spiral-matrix-ii/) | 中等 | 用yield来写好方便~ |
| [921. 使括号有效的最少添加](https://leetcode-cn.com/problems/minimum-add-to-make-parentheses-valid/) | 中等 | 数学题，一次ac |
| [260. 只出现一次的数字 III](https://leetcode-cn.com/problems/single-number-iii/) | 中等 | 注意python求bin，如果是求补码，负数要 + 2 ** 32 次方 |
| [48. 旋转图像](https://leetcode-cn.com/problems/rotate-image/) | 中等 | yield 简直是太好用了~ |
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
| [648. 单词替换](https://leetcode-cn.com/problems/replace-words/) | 中等 | 可以用前缀树来解 |
| [215. 数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/) | 中等 | 用二分，结果还没有内置的排序快。。。 |
| 稍微长一点的文本 | 短文本 | 中等文本 |


---
# 没有解出的题
+ 1020.飞地的数量 深搜超时， 38/58
+ 1043.分隔数组以得到最大和 记忆化递归超时 14 / 52 个通过测试用例
    + 原因是求最大值的时候，要重复计算，这很低效，可以优化。(已通过，使用记忆化递归)
+ 638.大礼包  深搜超时，因为多重背包当成了一重？