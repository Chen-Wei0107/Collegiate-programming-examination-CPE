#GCD
import math

while True:  # 進入無限循環
    N = int(input())  # 讀取正整數 N

    if N == 0:
        break  # 如果 N 等於 0，則結束循環

    G = 0  # 初始化 G 為 0，用於存儲 GCD 總和

    for i in range(1, N + 1):
        for j in range(i + 1, N + 1):
            G += math.gcd(i, j)  # 計算 i 和 j 之間的 GCD，並將結果加到 G 中

    print(G)  # 輸出 GCD 總和
