while True:
    N,M=map(int,input().split())
    print(N,M)
    if M==0 and N==0:
        break
    num=[]
    for _ in range(N):
        num.append(int(input()))
    def cmp(x):#4種key k1,k2,k3,k4=(k1)餘數大小排序,(k2)奇(0)在偶(1)前,(k3)大奇數在小奇數前,(k4)小偶數在大偶數前
        if x<0:
            pn=-1
        else:
            pn=1
        k1=abs(x) % M * pn
        
        if x%2!=0:
            k2,k3,k4=0,-x,0

        else:
            k2,k3,k4=1,x,0,
        return k1,k2,k3,k4

    num.sort(key=cmp)
    for i in num:

        print(i)
