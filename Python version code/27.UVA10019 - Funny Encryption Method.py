N=int(input())
for _ in range(N):
    m=input()
    m1=bin(int(m,10))
    b1=list(m1).count("1")
    m2=bin(int(m,16))
    b2=list(m2).count("1")
    print(b1,b2)