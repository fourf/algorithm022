学习笔记

1. 分治 + 回溯 + 递归 + 动态规划（动态递推）
   
    本质：将复杂问题分解为各种子问题，同时寻找重复性

2. 写递归程序方法论（本质：寻找重复性）
   
   - 人肉递归低效、很累，要抵制人肉递归

   - 找到最近最简方法，将其拆解成可重复解决的子问题

   - 数学归纳法思维

3. 动态规划（动态递推）：分治 + 最优子结构
   
   关键点

   - 动态规划和递归、分治没有根本上的差别（关键看有无最优子结构）

   - 共性：找到重复子问题

   - 差异性：最优子结构，中途可以淘汰次优解

   解法：
    
   - 自顶向下：递归加记忆化搜索

   - 自底向上：循环（找递推公式）
  
     步骤：1、寻找最优子结构；2、状态数组定义；3、递推方程（DP方程、状态转移方程）