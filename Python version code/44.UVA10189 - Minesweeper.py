num=0
flag=False
while True:
    n,m=map(int,input().split())
    if(n==0 and m==0):
        break
    arr=[[0]*(m+2)]
    num+=1
    for _ in range(n):
        arr1=[0]+[x for x in input()[::1]]+[0]
        arr.append(arr1)
    arr.append([0]*(m+2))
    arr4=[]
    for i in range(1,n+1):
        arr3=[]#存放一列
        for j in range(1,m+1):
            count=0
            if(arr[i][j]=='*'):#存放地雷位置
                count='*'
                arr3.append(count)
                continue

            if(arr[i+1][j]=='*'):count+=1#檢查相鄰八個座標中有無地雷
            if(arr[i-1][j]=='*'):count+=1
            if(arr[i][j+1]=='*'):count+=1
            if(arr[i][j-1]=='*'):count+=1
            if(arr[i+1][j+1]=='*'):count+=1
            if(arr[i+1][j-1]=='*'):count+=1
            if(arr[i-1][j-1]=='*'):count+=1
            if(arr[i-1][j+1]=='*'):count+=1
            arr3.append(count)
        arr4.append(arr3)#把一列存到各行
    if flag==True:
        print()
    print(f'Field #{num}:')
    flag=True
    for i in arr4:
        print(*i,sep="")