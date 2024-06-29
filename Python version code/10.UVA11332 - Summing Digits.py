while True:  # 進入無限循環
    n = input()  # 讀取輸入的數字

    if n == "0":  # 如果輸入是 "0"，則結束循環
        break

    while len(n) > 1:  # 只要數字的長度大於1，就繼續計算數位根
        # 將數字的各位數加總，並將結果轉換為字串以便下一輪計算
        n = str(sum(list(map(int, n))))

    print(n)  # 輸出數位根
