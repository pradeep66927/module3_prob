## sum of given digit 
n=int(input("enter digit >> "))
su=0
while n !=0:
    d=n % 10
    su+=d
    n=n//10
print(su)

