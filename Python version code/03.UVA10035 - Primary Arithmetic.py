while True:
    name1, name2 = input().split(" ")  # 讀取兩個輸入的數字，以空格分隔
    if name1 == "0" and name2 == "0":
        break  # 如果兩個輸入都是 "0"，則結束循環

    k, temp = 0, 0  # 初始化進位次數 k 和進位補1的變數 temp

    # 讓兩個數字的長度相等，使用 zfill 函數在較短的數字前填充0
    if len(name1) > len(name2):
        name2 = name2.zfill(len(name1))
    elif len(name2) > len(name1):
        name1 = name1.zfill(len(name2))

    # 從右往左遍歷兩個數字，進行加法運算
    for i in range(len(name1) - 1, -1, -1):
        if (int(name1[i]) + int(name2[i]) + temp) >= 10:
            temp = 1  # 如果相加的結果大於等於10，設置進位補1
            k += 1  # 增加進位次數
        else:
            temp = 0  # 否則，進位補0

    # 根據進位次數輸出結果
    if k == 0:
        print("No carry operation.")
    elif k == 1:
        print(k, "carry operation.")
    else:
        print(k, "carry operations.")
