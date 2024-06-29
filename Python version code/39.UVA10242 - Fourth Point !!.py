import sys

for line in sys.stdin:
    points = list(map(float, line.strip().split()))

    # 提取前两个点作为第一个线段的两个端点
    x1, y1, x2, y2, x3, y3, x4, y4 = points[:8]

    # 查找共享的端点
    if x1 == x3 and y1 == y3:
        common_x, common_y = x1, y1
        x = x2 + x4 - x3
        y = y2 + y4 - y3
    elif x1 == x4 and y1 == y4:
        common_x, common_y = x1, y1
        x = x2 + x3 - x4
        y = y2 + y3 - y4
    elif x2 == x3 and y2 == y3:
        common_x, common_y = x2, y2
        x = x1 + x4 - x3
        y = y1 + y4 - y3
    elif x2 == x4 and y2 == y4:
        common_x, common_y = x2, y2
        x = x1 + x3 - x4
        y = y1 + y3 - y4
    else:
        break

    # 输出结果，保留3位小数
    print("{:.3f} {:.3f}".format(x, y))
