def degree(n):  # 定義計算一個數字各位數相加的函數
    k = 0
    for i in str(n):
        k += int(i)
    return k

while True:
    num = input()  # 讀取輸入的數字（作為字串）
    if num == "0":
        break  # 如果輸入是0，則結束循環

    n = int(num)  # 將輸入的數字轉換為整數
    count = 0

    while n % 9 == 0:
        n = degree(n)  # 連續計算各位數相加，直到得到的數字小於10
        count += 1

        if n == 9:
            break  # 如果得到的數字是9，則停止計算

    if count > 0:
        # 輸出結果，若count大於0，表示該數字是9的倍數且有9級
        print("{} is a multiple of 9 and has 9-degree {}.".format(num, count))
    else:
        # 輸出結果，若count等於0，表示該數字不是9的倍數
        print("{} is not a multiple of 9.".format(num))
