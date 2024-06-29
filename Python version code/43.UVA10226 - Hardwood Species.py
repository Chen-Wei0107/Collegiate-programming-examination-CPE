T =int(input())
input()
for _ in range(T):
    treename=[]
    treenum={}
    while True:
        try:
            word=input()
            if word !="":
                treename.append(word)
            else:
                break
        except EOFError:
            break
    for i in sorted(set(treename)):
        print(i,format(treename.count(i)/len(treename)*100,".4f"))
    if _ !=(T-1):
        print()