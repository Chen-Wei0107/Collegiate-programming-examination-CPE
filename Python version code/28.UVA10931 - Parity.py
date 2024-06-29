while 1:
    name=int(input())
    if name==0:
        break
    name=bin(name)
    print("The parity of",name[2:],"is",name.count("1"),"(mod 2).")
"""
while 1:
    name=int(input())
    if name==0:
        break
    name=bin(name).replace("0b","")
    print("The parity of",name,"is",list(name).count("1"),"(mod 2).")
"""
