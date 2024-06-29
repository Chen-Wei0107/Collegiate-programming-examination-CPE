while True:  # 進入無限循環
    a, b = map(int, input().split(" "))  # 讀取 a 和 b

    ans = 0  # 初始化答案為0

    if a == 0 and b == 0:
        break  # 如果 a 和 b 都是0，則結束循環

    for i in range(a, b + 1):  # 遍歷範圍 [a, b] 內的每個數字
        if i ** 0.5 % 1 == 0:  # 檢查是否為完全平方數
            ans += 1  # 如果是完全平方數，將答案加1

    print(ans)  # 輸出在範圍 [a, b] 內的完全平方數的數量
