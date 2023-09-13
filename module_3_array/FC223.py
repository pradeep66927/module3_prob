## Baby weight related questions 
n=int(input("enter num of baby >> "))
l=[0]*n
for i in range(n):
    weight=int(input("baby weight >> "))
    l[i]=weight
# mean=0
mx=0
mn=l[0]
su=0
count=0
for j in l:
    su+=j
    count+=1
    if j > mx:
        mx=j
    if j < mn:
        mn=j
print("mean weight of baby >> ",su/count)
print("maximum wight >>",mx)
print("minimum weight >>",mn)


