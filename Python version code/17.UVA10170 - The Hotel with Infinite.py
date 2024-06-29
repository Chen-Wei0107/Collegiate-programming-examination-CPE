from sys import stdin
import math

# 从标准输入读取数据
for f in stdin:
    all = 0

    # 读取输入数据，S 和 D 为两个整数
    S, D = map(int, f.split())

    # 根据给定的公式计算 ans
    # f = (2 * D) + (S^2) - S
    f = (2 * D) + (S ** 2) - S
    ans = (-1 + ((1 - (4 * (-f))) ** 0.5)) / 2

    # 向上取整并打印结果
    print(math.ceil(ans))
