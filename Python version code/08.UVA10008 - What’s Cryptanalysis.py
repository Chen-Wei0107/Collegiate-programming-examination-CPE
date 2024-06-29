T = int(input())  # 讀取測試案例的數量
string = []  # 用於存儲所有測試案例的字母
ans = []  # 用於存儲轉換後的字母

# 讀取每個測試案例的字母，並將它們轉換為大寫
for _ in range(T):
    string += list(input())

for i in string:
    if i.islower():  # 如果字母是小寫
        ans.append(chr(ord(i) - 32))  # 將其轉換為大寫並添加到 ans 列表中
    elif i.isupper():  # 如果字母是大寫
        ans.append(i)  # 直接添加到 ans 列表中

string.clear()  # 清空原始字串列表
num = []  # 用於存儲出現次數的列表

# 使用 set 找出所有不重複的字母
for j in set(ans):
    string.append([j, ans.count(j)])  # 將字母和它出現的次數添加到 string 列表中
    num.append(ans.count(j))  # 將出現次數添加到 num 列表中

num = list(set(num))  # 使用 set 找出所有不重複的出現次數
string.sort()  # 將 string 列表按字母排序
num.sort(reverse=True)  # 將出現次數降序排列

# 遍歷出現次數，並打印對應的字母和次數
for k in num:
    for j in string:
        if k == j[1]:
            print(j[0], j[1])
