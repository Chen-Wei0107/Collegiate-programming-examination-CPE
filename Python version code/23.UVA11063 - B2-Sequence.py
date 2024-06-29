C = 0  # 初始化測試案例的計數器

while True:  # 進入無限循環
    C += 1  # 每次測試案例遞增計數器
    N = input()  # 讀取數列的長度 N
    num = list(map(int, input().split(" ")))  # 讀取 N 個數列元素

    ans = []  # 用於存儲 num[i] + num[j] 的值

    # 使用兩個嵌套迴圈遍歷所有可能的 i 和 j
    for i in range(len(num)):
        for j in range(i + 1, len(num)):
            ans.append(num[i] + num[j])  # 計算並添加 num[i] + num[j] 的值到 ans 中

    # 如果 ans 中的值都不重複，則數列是 B2-Sequence
    if len(ans) == len(set(ans)):
        print("Case #{}: It is a B2-Sequence.".format(C))
    else:
        print("Case #{}: It is not a B2-Sequence.".format(C))

    print()  # 輸出空行，用於區分不同的測試案例
    input()  # 等待用戶輸入，可選操作，用於控制程式的執行
