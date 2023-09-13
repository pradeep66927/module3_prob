## second max find 
n=int(input("enter n >>>"))
l=[None]*n
for i in range(n):
    l[i]=int(input("no >>> "))
m1=0
m2=0
for j in range(n):
    if l[j]>m1:
        m2=m1
        m1=l[j]
    else:
        if l[j]>m2:
            m2=l[j]
print(m2)



###  bubble sort method to sorting list
# for j in range((n-1),0,-1):
#     for k in range(j):
#         if l[k] > l[k+1]:
#             t=l[k]
#             l[k]=l[k+1]
#             l[k+1]=t 

