T=int(input())
for _ in range(T):
    N=int(input())
    P=int(input())
    p=[]
    day=[]
    ans=0
    for _ in range(P):
        p.append(int(input()))
    for i in range(P):
        D=0
        while D+p[i]<=N:
            D+=p[i]
            day.append(D)
    day=sorted(day)
    day=list(set(day))
    for i in range(len(day)):
        if day[i]%7!=6 and day[i]%7!=0:
            ans+=1
    print(ans)
