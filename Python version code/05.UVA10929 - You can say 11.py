while True:  # 進入無限循環
    n = int(input())  # 讀取一個整數

    if n == 0:  # 如果輸入的數字是0，則結束循環
        break

    if n % 11 == 0:  # 檢查輸入的數字是否是11的倍數
        print(n, "是11的倍數.")
    else:
        print(n, "不是11的倍數.")
