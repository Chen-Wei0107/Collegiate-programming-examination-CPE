while True:
    nums = input().split()  # 讀取輸入的整數序列，將其拆分為列表
    n = int(nums[0])  # 第一個數字是序列長度 n
    sequence = list(map(int, nums[1:]))  # 其餘數字是整數序列

    abs_seq = []  # 用於存儲相鄰數字的絕對差值

    for i in range(1, n):
        absolute_diff = abs(sequence[i] - sequence[i - 1])  # 計算相鄰數字的絕對差值

        # 如果絕對差值在 1 到 n-1 之間，則將其添加到 abs_seq 中，否則結束迴圈
        if 1 <= absolute_diff < n:
            abs_seq.append(absolute_diff)
        else:
            break

    # 如果 abs_seq 中的唯一值數量等於 n-1，則是 Jolly 跳躍數列
    if len(set(abs_seq)) == (n - 1):
        print("Jolly")
    else:
        print("Not jolly")
