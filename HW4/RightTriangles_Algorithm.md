# 直角三角形计数算法设计

## 问题分析

给定n个二维平面上的点，计算能够构成直角三角形的三点组合数量。

### 算法复杂度分析

| 方法 | 时间复杂度 | 空间复杂度 | 适用性 |
|------|------------|------------|--------|
| 暴力枚举 | O(n³) | O(1) | n < 1000 |
| 固定直角顶点法 | O(n²) | O(n) | n < 10000 |
| 优化向量法 | O(n² log n) | O(n) | 大规模数据 |

## 最优解法：固定直角顶点法

### 核心思想

1. **枚举直角顶点**：对每个点作为直角顶点进行计算
2. **向量计算**：计算该点到其他所有点的向量
3. **垂直判定**：利用向量点积为0判断垂直关系
4. **计数优化**：使用哈希表统计相同方向的向量数量

### 数学原理

对于三个点A、B、C构成直角三角形：
- 设B为直角顶点
- 向量BA和向量BC垂直
- 数学条件：BA · BC = 0

### 精度处理策略

为避免浮点数精度问题，使用以下技巧：
1. **最大公约数约简**：将向量(dx, dy)约简为最简形式
2. **符号标准化**：确保向量表示的唯一性
3. **整数运算**：避免浮点数比较

## 伪代码

```
算法：CountRightTriangles
输入：points[] - n个二维点的数组
输出：count - 直角三角形的数量

BEGIN
    count = 0
    
    FOR each point P in points:
        // 创建方向向量的哈希表
        direction_map = new HashMap()
        
        FOR each other point Q in points:
            IF P != Q:
                // 计算向量PQ
                dx = Q.x - P.x
                dy = Q.y - P.y
                
                // 标准化向量（避免精度问题）
                gcd = GCD(abs(dx), abs(dy))
                IF gcd > 0:
                    dx = dx / gcd
                    dy = dy / gcd
                
                // 确保向量表示唯一性
                IF dx < 0 OR (dx == 0 AND dy < 0):
                    dx = -dx
                    dy = -dy
                
                // 统计该方向的向量数量
                direction = (dx, dy)
                direction_map[direction] += 1
        
        // 计算以P为直角顶点的直角三角形数量
        FOR each direction (dx, dy) in direction_map:
            // 寻找垂直方向 (-dy, dx)
            perpendicular = (-dy, dx)
            IF perpendicular in direction_map:
                count += direction_map[direction] * direction_map[perpendicular]
    
    // 每个直角三角形被计算了一次（以直角顶点为基准）
    RETURN count
END

函数：GCD(a, b)
BEGIN
    WHILE b != 0:
        temp = b
        b = a % b
        a = temp
    RETURN a
END
```

## 算法优化要点

### 1. 向量标准化
```
标准化向量(dx, dy):
1. 计算gcd = GCD(|dx|, |dy|)
2. dx = dx / gcd, dy = dy / gcd
3. 如果dx < 0 或 (dx == 0 且 dy < 0): dx = -dx, dy = -dy
```

### 2. 垂直向量关系
```
向量(a, b)的垂直向量是(-b, a)或(b, -a)
我们选择(-b, a)作为标准垂直向量
```

### 3. 计数策略
```
对于每个方向向量，如果有m个点在该方向，n个点在垂直方向
则以当前点为直角顶点的直角三角形数量为 m × n
```

## 时间复杂度分析

- **外层循环**：O(n) - 枚举每个点作为直角顶点
- **内层循环**：O(n) - 计算到其他点的向量
- **哈希表操作**：O(1) 平均情况
- **总体复杂度**：O(n²)

## 空间复杂度分析

- **哈希表存储**：最多O(n)个不同方向
- **总体空间复杂度**：O(n)

## 正确性证明

1. **完整性**：算法枚举了所有可能的直角顶点
2. **准确性**：通过向量点积准确判断垂直关系
3. **无重复**：每个直角三角形只在其直角顶点处被计算一次