学习笔记

1. 位运算

    将x最右边的n位清零：x & (~0 << n)

    获取x的第n位值（0或1）：(x >> n) & 1

    获取x的第n位的幂值：x & (1 << n)

    仅将第n位置为1：x | (1 << n)

    仅将第n位置为0：x & (~(1 << n))

    将x最高位至第n位（含）清零：x & ((1 << n) - 1)

2. 位运算实战要点

    - 判断奇偶：
    
        x % 2 == 1 => x & 1 == 1

        x % 2 == 0 => x & 1 == 0

    - x / 2 => x >> 1
    - x = x & (x - 1) 清零最低位的1
    - x & -x 得到最低位的1
    - x & (~x) = 0

3. 布隆过滤器（Bloom Filter）

    一个很长的二进制向量和一系列随机映射函数，，可以用于检索一个元素是否在一个集合中

    优点：空间效率和查询效率要远远超过一般的算法

    缺点：有一定的误识别率和删除困难

4. LRU cache

    两个要素：大小，替换策略

    hash table + DoubleLinkList

    O(1)查询、修改、更新