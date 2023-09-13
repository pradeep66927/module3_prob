p=int(input("lower : "))
q=int(input(" upper :"))
s=0
for i in range(p,q+1):
    if i%p==0:
        if  i%q !=0:
            s+=i
print(s)
