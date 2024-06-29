string=list(input().split(" "))
if len(string)==5:
	T=int(string[0])
	for i in range(1,T+1):
		x1,y1,x2,y2=map(int,string[1:])
		if x1==0 and y1==0:
			step1=0
		else:
			n=x1+y1-1
			step1 = (n * n + 3 * n) / 2 + (x1 + 1)
		if x2==0 and y2==0:
				step2=0
		else:
			n=x2+y2-1
			step2 = (n * n + 3 * n) / 2 + (x2 + 1)
		print("Case {}: {}".format(i,int(step2-step1)))

elif len(string)==1:
	T=int(string[0])
	for i in range(1,T+1):
		x1,y1,x2,y2=map(int,input().split(" "))
		if x1==0 and y1==0:
			step1=0
		else:
			n=x1+y1-1
			step1 = (n * n + 3 * n) / 2 + (x1 + 1)
		if x2==0 and y2==0:
				step2=0
		else:
			n=x2+y2-1
			step2 = (n * n + 3 * n) / 2 + (x2 + 1)
		print("Case {}: {}".format(i,int(step2-step1)))
