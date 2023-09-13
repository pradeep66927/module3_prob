### Third max find *********
n=int(input("enter n>>>> "))
l=[None]*n
for i in range(n):
    l[i]=int(input('enter >>> '))
m1=0
m2=0
m3=0
for j in range(n):
    if l[j]>m1:
        m3=m2
        m2=m1
        m1=l[j]
    elif l[j]> m2:
        m3=m2
        m2=m1
    else:
        m3=l[j]
print(m3)

