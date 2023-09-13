## find sum which are given by user as input n term 
n=int(input("enter n >>> "))
su=0
for i in range(n):
    num = int(input("no >> "))
    su+=num
print(su)