n=int(input("enter n >>"))
l=[None]*n
for i in range(n):
    l[i]=int(input(">>> "))
m=mi=l[0]
for j in l:
    print(j)
    for j in l:
        if j > m:
            m=j 

        if j < mi:
            mi=j
print("max num :",m)
print("min num :",mi)