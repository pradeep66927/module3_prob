## user two sorted array find median 

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

for l in range(n3):
    for m in range(n3-l-1):
        if l3[m] > l3[m+1]:
            l3[m],l3[m+1]=l3[m+1],l3[m]
print(l3)
if n3 % 2 ==0:
    for n in range((n3//2)+1):
        med1=l3[n-1]
        med2=l3[n]
        med=(med1+med2)/2
else:
    for o in range((n3//2)+1):
        med=l3[(n3//2)+1]

print("median of two array >> ",med)