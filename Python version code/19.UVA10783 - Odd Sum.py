case = int(input())  # 讀取測試案例的數量

for i in range(0, case):  # 遍歷每個測試案例
    A, B = int(input()), int(input())  # 讀取範圍的起始值 A 和結束值 B

    sum = 0  # 初始化總和為0

    # 使用 for 循環遍歷範圍 [A, B] 內的數字
    for k in range(A, B + 1, 1):
        if k % 2 == 1:  # 如果數字 k 是奇數
            sum += k  # 將奇數 k 添加到總和中

    # 輸出結果，注意這裡使用了 f-string 格式化輸出
    print(f"Case {i + 1}:", sum)
