# 初始化 Fibonacci 數列的前兩個數字
a = [1, 2]
for i in range(2, 40):
    # 生成 Fibonacci 數列
    a.append(a[i-1] + a[i-2])

n = int(input())  # 輸入要處理的數量
for i in range(n):
    m = int(input())  # 輸入要轉換成 Fibonacci 二進制的數字
    print("{} = ".format(m), end="")

    c = 0  # 計數用變數，用來判斷是否在 Fibonacci 數列中
    for j in range(39, -1, -1):  # 從最大的 Fibonacci 數字開始檢查
        if m // a[j] == 1:
            print("1", end="")  # 如果 m 大於等於當前 Fibonacci 數字，輸出 1
            m %= a[j]  # 更新 m，減去當前 Fibonacci 數字
            c += 1
        elif c > 0 and m // a[j] == 0:
            print("0", end="")  # 如果 m 小於當前 Fibonacci 數字，輸出 0

    print(" (fib)")  # 輸出 (fib) 表示結果為 Fibonacci 二進制


"""
# 定义一个递归函数来计算斐波那契数列的第 n 个值
def Fibonacci(n): 
    if n > 1:                      
        return Fibonacci(n-1) + Fibonacci(n-2)  
    return n

fib_list = []  # 存储斐波那契数列的列表
for i in range(2, 40):
    fib_list.append(Fibonacci(i))  # 生成斐波那契数列的前40个值
fib_list.sort(reverse=True)  # 逆序排列斐波那契数列

T = int(input())  # 读取测试案例数量
for _ in range(T):
    n = int(input())  # 读取目标正整数

    k = n
    ans = []  # 存储目标数 n 表示为斐波那契数列和的指标
    for i in fib_list:
        if i <= k and k > 0:
            k -= i
            ans.append(len(fib_list) - fib_list.index(i))  # 计算指标

    representation = []  # 存储二进制表示形式
    for i in range(max(ans), 0, -1):
        if i in ans:
            representation.append("1")
        else:
            representation.append("0")

    # 输出结果
    print("{} = {} (fib)".format(n, "".join(representation)))
"""