## have to find union and intersection or array

n1=int(input("enter nuber of term want to take in first array >> "))
l1=[0]*n1
for i in range(n1):
    l1[i]=int(input("enter number >> "))

n2=int(input(" enter number of term want to take in 2nd array >>> ")) 
l2=[0]*n2
for j in range(n2):
    l2[j]=int(input("enter number "))
n3=n1+n2

uni_l=[0]*(n3)
for p in l2:
    if p not in uni_l:
        uni_l=uni_l + [p]
uni_l2=[q for q in uni_l if q !=0]
print("union ele :",uni_l2)


intersec_l=[0]*(10)
for k in l1:
        if k in l2:
            intersec_l[k]=k 
intersec_l2=[o for o in intersec_l if o !=0]
print("intersection ele : ",intersec_l2)



