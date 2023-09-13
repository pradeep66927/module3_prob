## 
n1=int(input("enter nuber of term want to take in first array >> "))
l1=[0]*n1
for i in range(n1):
    l1[i]=int(input("enter number >> "))

n2=int(input(" enter number of term want to take in 2nd array >>> ")) 
l2=[0]*n2
for j in range(n2):
    l2[j]=int(input("enter number "))
n3=n1+n2
l3=l1+l2
print(l3)

for k in range(n3):
    for l in range(n3-k-1):
        if l3[l] > l3[l+1]:
            t=l3[l]
            l3[l]=l3[l+1]
            l3[l+1]=t
print(l3)
        






