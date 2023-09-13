## M row and N column input pattern solid rectangle
m=int(input("enter row >> "))
n=int(input("enter column >> "))
for i in range(m):
    s=""
    for j in range(n):
        s+="*"
    print(s)