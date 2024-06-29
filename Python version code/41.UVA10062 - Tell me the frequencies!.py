c = 0
while True:
	
	n = input()
	
	
	a = [0 for i in range(257)]
	for i in n:
		a[ord(i)] += 1
	
	if c > 0:
		print()
	c += 1
		
	for i in range(1, len(n)+1):
		for j in range(256, 0, -1):
			if a[j] == i:
				print(j, i)