import string

while True:  # 進入無限循環
    n = input()  # 讀取數字字符串 n
    base = string.digits + string.ascii_uppercase + string.ascii_lowercase
    sum1, max0 = 0, 1  # max0 => 裡面最大的數字，因為進制不能比它小

    if n[0] == "+" or n[0] == "-":
        n = n.lstrip(n[0])  # 移除正負號

    for i in n:
        r = base.index(i)  # 找出字符 i 在 base 中的索引
        if r > max0:
            max0 = r
        sum1 += r  # 將字符對應的索引值加入總和 sum1 中

    flag = 0

    for j in range(max0-1, 63):  # 從 max0 開始遍歷可能的進制
        if sum1 % (j + 1) == 0:  # 如果數字的總和能被 (j+1) 整除
            flag = j + 2  # 將 flag 設置為進制值
            break

    if flag > 0:
        print(flag)  # 輸出找到的進制值
    else:
        print("such number is impossible!")  # 找不到符合條件的進制，輸出 "such number is impossible!"
