import statistics  # 導入 statistics 模組，用於計算中位數

t = int(input())  # 讀取測試案例的數量

for _ in range(t):  # 遍歷每個測試案例
    num = []  # 創建一個空列表 num，用於存儲輸入的數字
    sum1 = 0  # 初始化總和為 0

    num = list(map(int, input().split(" ")))  # 讀取一行輸入並將數字轉換為整數列表
    home = statistics.median_high(num[1:])  # 使用 statistics 模組計算中位數，排除第一個數字（表示個數）
    
    # 遍歷除第一個數字以外的所有數字，計算絕對差的總和
    for i in range(1, num[0] + 1):
        sum1 += abs(num[i] - home)

    print(sum1)  # 輸出總和
