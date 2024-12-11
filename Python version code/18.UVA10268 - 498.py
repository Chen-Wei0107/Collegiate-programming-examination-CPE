def derivative(x, a):
    max = len(a) - 1
    sum, exp, i = 0, 1, (max - 1)
    while i >= 0:
        k = (a[i] * exp * (max - i))
        sum += k
        exp *= x
        i -= 1
    return sum

while True:
    try:
        x = int(input())  # 讀取 x 的值
        A = list(map(int, input().split(" ")))  # 讀取係數列表 A

        # 調用 derivative 函數計算多項式在 x 點的導數
        result = derivative(x, A)

        print(result)  # 輸出計算結果
    except EOFError:
        break