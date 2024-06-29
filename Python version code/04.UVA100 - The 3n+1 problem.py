# 定義一個函數f，用於計算下一個數字
def f(n):
    if n % 2 != 0:
        return n * 3 + 1
    else:
        return n // 2

while True:
    num = []  # 用於存儲結果的列表
    i, j = map(int, input().split(" "))  # 讀取輸入的兩個數字i和j

    # 確保max1是較大的數，min1是較小的數
    if j < i:
        max1 = i
        min1 = j
    else:
        max1 = j
        min1 = i

    # 對於min1到max1之間的每個數k，計算它的"循環長度"
    for k in range(min1, max1 + 1):
        l = 1  # 初始化"循環長度"為1
        while True:
            if k == 1:
                num.append(l)  # 如果k變成1，表示計算結束，將循環長度添加到num列表中
                break
            k = f(k)  # 使用函數f計算下一個數字
            l += 1  # 增加循環長度

    # 輸出i、j以及計算得到的最大循環長度
    print(i, j, max(num))
