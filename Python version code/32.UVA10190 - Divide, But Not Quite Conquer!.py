while True:  # 進入無限循環
    n, m = map(int, input().split(" "))  # 讀取 n 和 m

    k = []  # 用於存儲整數序列

    k.append(n)  # 將 n 添加到整數序列中

    if m > 1:
        while n % m == 0:
            n //= m  # 連續除以 m
            k.append(n)  # 如果仍然能整除，則將結果添加到整數序列中
            if n % m != 0 and n > 1:
                k.clear()  # 如果不能整除，或者 n 不大於1，則清空整數序列
                break

    if len(k) <= 1:
        print("Boring!")  # 如果整數序列長度不大於1，則輸出 "Boring!"
    else:
        print(" ".join(str(i) for i in k))  # 否則，輸出整數序列的元素，並用空格分隔



"""
while 1:
    n,m=map(int,input().split(" "))
    k=[]
    k.append(n)
    while m>1 and n%m==0:
        n=n/m
        k.append(int(n))
        if n%m!=0 and n>1:
            k.clear()
            break
    if len(k)<=1 :
        print("Boring!")
    else :
        print(" ".join(str(i) for i in k))
"""