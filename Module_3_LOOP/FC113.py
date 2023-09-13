n=int(input("how much input>>>"))
l=[0]*n
for i in range(n):
    n1=int(input("enter number >>"))
    l[i]=n1
    mn_num=n1
    if mn_num > n1:
        mn_num=n1

hcf=0
for j in range(1,mn_num):
    c=0
    for k in l:
        if k % j == 0:
            c+=1
    if c == n:
        hcf=j
print("HCF of n number = ",hcf)



