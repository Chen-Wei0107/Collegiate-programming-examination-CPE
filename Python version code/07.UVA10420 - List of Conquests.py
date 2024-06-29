T = int(input())  # 讀取測試案例的數量
con = []  # 創建一個空列表 con，用於存儲名字

# 讀取每個測試案例中的名字，並將其添加到 con 列表中
for _ in range(T):
    name = list(input().split(" "))  # 讀取名字，假設名字不包含空格
    con.append(name[0])

con = sorted(con)  # 將名字列表按字母順序排序
k = sorted(list(set(con)))  # 使用 set 找出不重複的名字，並按字母順序排序

# 遍歷每個不重複的名字，並計算它在原始列表中出現的次數
for i in range(len(k)):
    print(k[i], con.count(k[i]))  # 輸出名字和它的出現次數

