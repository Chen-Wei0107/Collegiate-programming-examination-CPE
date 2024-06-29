def is_prime(num):
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def erimp(num):
    if int(num) <= 11 or num[::-1] == num:
        return False
    return is_prime(int(num[::-1]))

while True:  # 進入無限循環
    num = int(input())  # 讀取一個整數

    ans = is_prime(num)  # 檢查是否為質數

    if ans == True:
        if erimp(str(num)) == True:
            print(num, "is emirp.")  # 如果是質數且是emirp，輸出 "is emirp."
        else:
            print(num, "is prime.")  # 如果是質數但不是emirp，輸出 "is prime."
    else:
        print(num, "is not prime.")  # 如果不是質數，輸出 "is not prime."
