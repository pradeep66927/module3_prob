### perfect number 
n=int(input("enter to check perfect no: "))
fac_su=0
for i in range(1,n):
    if n % i == 0:
        fac_su+=i       
if fac_su == n:
    print(n," is a perfect number ")
else:
    print(n," is not a perfect number")
