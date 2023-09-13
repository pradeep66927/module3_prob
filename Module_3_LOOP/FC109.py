## factorial sum of user input
n= int(input("enter no: "))
su=0
mu=1
for i in range(1,n+1):
    mu*=i
    su+=mu
print(su)
