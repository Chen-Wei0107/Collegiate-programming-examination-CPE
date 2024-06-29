import statistics

while True:
    num = []
    N = int(input())  # 輸入數量

    # 每個輸入寫入數列
    for _ in range(N):
        num.append(int(input()))

    num.sort()  # 对整数列表排序

    maxmedian = statistics.median_high(num)  # 找到中位数的上中位数（如果有）
    minmedian = statistics.median_low(num)   # 找到中位数的下中位数（如果有）

    if len(num) % 2 != 0:  # 如果整数数量是奇数
        print(minmedian, num.count(minmedian), 1)
    else:  # 如果整数数量是偶数
        if minmedian == maxmedian:  # 如果上中位数等于下中位数，只需計算一次避免重複計算
            print(minmedian, num.count(minmedian), maxmedian - minmedian + 1)
        else:
            print(minmedian, num.count(minmedian) + num.count(maxmedian), maxmedian - minmedian + 1)#中位數之間的各數都會相等
