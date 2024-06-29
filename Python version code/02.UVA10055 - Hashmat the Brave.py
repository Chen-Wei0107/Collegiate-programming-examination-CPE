while True:  # 進入無限循環
    a, b = map(int, input().split(" "))  # 讀取兩個整數，以空格分隔，並將它們轉換為整數

    if a > 2**32 or b > 2**32:  # 檢查 a 和 b 是否大於 2 的 32 次方
        break  # 如果其中一個大於 2 的 32 次方，則結束循環

    result = abs(b - a)  # 計算 b 和 a 的差的絕對值
    print(result)  # 輸出結果
