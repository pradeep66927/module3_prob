## lcm and hcf 

n1=int(input("enter 1st num >> "))
n2=int(input("enter 2nd num >>"))
if n1<n2:
    n1,n2=n2,n1
hcf=0
for i in range(1,n1):
    if n1 % i == 0:
        if n2 % i ==0:
            hcf=i
lcm=(n1*n2)//hcf
print("lcm= ",lcm)
print("hcf= ",hcf)

