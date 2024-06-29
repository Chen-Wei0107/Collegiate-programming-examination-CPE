T = int(input())  # 讀取測試案例的數量

for _ in range(T):  # 遍歷每個測試案例
    absum, abdifference = map(int, input().split(" "))  # 讀取 absum 和 abdifference

    # 檢查是否存在符合條件的解
    # 條件1：差異不能大於總和，否則無法找到合適的 a 和 b
    # 條件2：(a + b) 必須為偶數，因為 (absum + abdifference) / 2 必須是整數
    if abdifference > absum or (abdifference + absum) % 2 != 0:
        print("impossible")  # 找不到解，輸出 "impossible"
    else:
        a = (abdifference + absum) // 2  # 計算 a 的值
        b = absum - a  # 計算 b 的值
        print(a, b)  # 輸出 a 和 b
