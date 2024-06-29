import math

while True:
    name = input().split()
    s = int(name[0]) + 6440  # 地球半径加上卫星高度
    a = int(name[1])  # 仰角
    angle = name[2]  # 角度单位

    if angle == "min":
        a = a / 60  # 如果单位是角分，将角度转换为度 1°（度）= 60′（角分）

    arc_distance = s * 2 * math.pi * a / 360  # 弧长 = 2 * 半径 * PI * (角度/360)
    chord_distance = math.sin(math.radians(a) / 2) * s * 2  # 弦长 = sin(弧度/2) * 半径 * 2

    # 输出结果，保留6位小数
    print(format(arc_distance, '.6f'), format(chord_distance, '.6f'))
