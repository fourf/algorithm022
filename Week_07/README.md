学习笔记

1. 字典树（trie）
   
   - 数据结构
 
        python 使用 dict 来动态实现

   - 核心思想

        空间换时间

        利用字符串的公共前缀来降低查询时间的开销以达到提高效率的目的

   - 基本性质
        
        节点本身不存完整单词

        从根节点到某一节点，路径上经过的字符串连接起来，为该节点对应的字符串

        每个节点的所有子节点路径代表的路径都不相同

2. 并查集

    适用场景：组团、配对问题、找连通分量

    基本操作：建群、合并群、查找群主

3. 初级搜索 -> 高级搜索
   
    优化方式：不重复（fabonacci）、剪枝（生成括号问题）

    搜索方向：双向搜索（BFS）、启发式搜索（优先级搜索）

4. 平衡二叉树
    
    当二叉搜索树退化为链表时，查询性能下降，需要左右子树节点平衡

    种类：2-3 tree；AVL tree；B-tree；Red-black tree；splay tree；treap

5. AVL tree
  
    - balance factor（平衡因子）= {-1， 0， 1}
    
        左子树的高度减去右子树的高度（有时相反）

    - 通过旋转操作进行平衡
        
        左旋： 右右子树

        右旋： 左左子树

        左右旋： 左右子树

        右左旋： 右左子树

    - 不足
    
        节点需要存储额外信息，且调整次数频繁

6. 红黑树
   
   红黑树是一种近似平衡的二叉搜索树，它能够确保任何一个节点的左右子树的高度差小于两倍。

   - 5个特点

        每个节点要么是红色，要么是黑色

        根节点是黑色

        每个叶子节点（空节点）是黑色

        不能有相邻接的两个红色节点

        从任一节点到其每个叶子的所有路径都包含相同数目的黑色节点

    - 关键性质

        从根到叶子的最长的可能路径不多于最短的可能路径的两倍长

    - AVL 和红黑树对比

        AVL 严格平衡，查找性能更好

        红黑树提供更快的插入、删除操作，平衡要求相对较松

        AVL 节点需要存储额外信息（平衡因子，高度），内存空间消耗大，红黑树只需要一个bit来存红或黑

7. 课后作业
   
   7.1 单词搜索II 使用前缀树的时间复杂度为O(m * n * 4^k)(m,n 为board的行数和列数，k为单词平均长度)，详细代码可查看作业

   7.2 双向 BFS 代码模板

```python
    def BFS(graph, start, end):
        visited = set()
        front = {start}
        back = {end}
        while front: 
            for node in front:
                visited.add(node)	
                process(node) 		
                nodes = generate_related_nodes(node) 		
                new_front.add(nodes)
            front = new_front
            if len(back) < len(front):
                front, end = end, front	
            # other processing work
             ...
```

