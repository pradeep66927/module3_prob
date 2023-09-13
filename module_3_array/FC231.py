## rotate array
n=int(input("enter the term require >> "))
a=[0]*n
for i in range(n):
    a[i]=int(input('enter number : '))
print(a)
i=0
j=0
k=0
g=1
b=[0]*n
p=int(input("enter position skip >> "))
while n > j:
    if a[i] != "*":
        if g == p:
            b[k]=(a[i])
            a[i]="*"
            j+=1
            k+=1
            g=1
        else:
            g+=1
    i=(i+1)%n
print(b)