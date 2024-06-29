def solve(n, p, i):
    if p == 0: 
        return f'{0:.4f}'
    q = (1 - p)
    return f'{p * (q ** (i - 1) / (1 - q ** n)):.4f}'

T = int(input())  # 讀取測試案例的數量

for t in range(T):  # 遍歷每個測試案例
    n, p, i = input().split()  # 讀取 n、p 和 i 並分別轉換為整數和浮點數

    # 調用 solve 函數計算目標事件成功的機率，並輸出結果
    print(solve(int(n), float(p), int(i)))
