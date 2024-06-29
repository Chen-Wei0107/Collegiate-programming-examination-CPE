Bangla_numbers = {10000000: "kuti", 100000: "lakh", 1000: "hajar", 100: "shata"}
count = 0
while True:
    flag = False
    count += 1
    remainder = int(input())  # 讀取輸入的整數

    if remainder == 0:
        print("   " + str(count) + ".", 0)
        continue
    
    ans = []  # 用於存儲孟加拉數字表示
    
    def division(value, i):
        if value // i > 0:
            ans.append(value // i)
            ans.append(Bangla_numbers[i])
            return (value % i)
        else:
            return value
    
    # 如果整數部分大於等於100，處理 'kuti' 部分
    if remainder // 10000000 >= 100:
        quotient = remainder // 10000000
        if quotient % 100 == 0 and remainder >= 1000000000:
            flag = True
        remainder = remainder % 1000000000
        for i in Bangla_numbers:
            quotient = division(quotient, i)
    
    # 如果 flag 為 True，表示有 'kuti'，添加 'kuti' 到 ans
    if flag == True:
        ans.append("kuti")
    
    # 處理其他部分，如 'lakh', 'hajar', 'shata' 等
    for i in Bangla_numbers:
        remainder = division(remainder, i)
    
    # 如果還有剩餘的數字，添加到 ans 中
    if remainder != 0:
        ans.append(remainder)
    
    # 輸出結果，使用 rjust 對齊
    print(str(count).rjust(4, " ") + ".", ' '.join(map(str, ans)))
