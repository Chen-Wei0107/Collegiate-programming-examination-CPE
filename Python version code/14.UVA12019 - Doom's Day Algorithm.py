T = int(input())  # 讀取測試案例的數量

M = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30]  # 每個月份的天數列表
week = ["Saturday", "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]  # 星期幾的列表

for _ in range(T):  # 遍歷每個測試案例
    mon, day = map(int, input().split(" "))  # 讀取輸入的月份和日期，假設月份從1開始

    for i in range(mon):
        day += M[i]  # 將指定月份之前的每個月份的天數相加，計算總天數

    # 根據總天數（day）計算星期幾
    # day % 7 將結果轉換為在星期列表（week）中的索引，並減去1以匹配星期的索引
    # 使用這個索引來找到對應的星期名稱
    print(week[day % 7 - 1])

