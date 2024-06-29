# 輸入測試次數
test = int(input())
text = ""

try:
    while True:
        text += input()
        text += ' '
except:
    pass

index = 0

# 定義一個函數，用於從輸入文本中提取數字
def getNumber():
    global index
    global text
    temp = ""
    while temp == "":
        while index < len(text):
            if text[index] == " ":
                index += 1
                break
            else:
                temp += text[index]
                index += 1
    return int(temp)

for _ in range(1, test + 1):
    if (_ != 1):
        print()
    print("Case {}:".format(_))
    cost = {}

    # 輸入每個進制的轉換成十進制的成本
    for i in range(0, 36):
        cost[i] = getNumber()

    case = getNumber()

    for c in range(0, case):
        num = getNumber()
        total = [0 for i in range(35)]

        # 計算每種進制的轉換成十進制的成本
        for i in range(2, 37):
            n = num

            while n > 0:
                total[i - 2] += cost[n % i]
                n //= i

        min_cost = min(total)

        print("Cheapest base(s) for number {}:".format(num), end="")

        # 找到最便宜的進制(s)
        for k in range(35):
            if total[k] == min_cost:
                print(" {}".format(k + 2), end="")
        print()
