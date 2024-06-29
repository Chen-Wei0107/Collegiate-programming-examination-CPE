T = int(input())  # 讀取測試案例的數量

for t in range(T):
    n=int(list(input().rstrip(" "))[-1])  # 讀取方陣的大小 n
    matrix = []  # 用於存儲矩陣的列表

    # 讀取 n x n 的矩陣
    for i in range(n):
        arr = list(map(int, input().split()))
        matrix.append(arr)

    flag = True  # 初始化標誌為 True，假設矩陣對稱

    # 使用兩個嵌套的迴圈遍歷矩陣的左上半部分
    for i in range(n):
        for j in range(i, n):
            if matrix[i][j] < 0 or matrix[n - 1 - i][n - 1 - j] < 0:
                flag = False  # 如果矩陣中有負數，則將標誌設置為 False
                break
            if matrix[i][j] != matrix[n - 1 - i][n - 1 - j]:
                flag = False  # 如果矩陣不對稱，則將標誌設置為 False
                break

    if flag == False:
        print(f'Test #{t + 1}: Non-symmetric.')  # 輸出非對稱
    else:
        print(f'Test #{t + 1}: Symmetric.')  # 輸出對稱
