## binary to decimal  
n=input("enter binary no >>> ")
d=0

c=0
for i in n:
    c+=1

for j in n:
    d+=int(j)*(2**int(c-1))

    c-=1
print("decimal",d)

