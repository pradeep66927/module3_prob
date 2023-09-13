## series of 2 + (2^2)/2 + (2^3)/3
x=int(input("enter base >> "))
n=int(input("enter power till go >> "))
s=x
su=0
for i in range(1,n+1):
    t=(s**i)/i
    su+=t
print(su)


## (ii) problem + , - series 
# x=int(input("enter base of series >> "))
# n=int(input("enter power till go >>"))
# su=0
# p=1
# for j in range(1,n+1):
#     if j % 2!=0:
#         su+=((x**p)/p)
#     else:
#         su-=((x**p)/p) 
#     p+=2
# print(su)


### ( 3rd ) problem + , - , factorial series 
# x=int(input("enter base of series >> "))
# n=int(input("enter power till go >> "))
# su=0
# p=1
# for j in range(1,n+1):
#     f=1
#     for k in range(1,p+1):
#         f*=k
#     if j % 2!=0:
#         su+=((x**p)/f)
#     else:
#         su-=((x**p)/f) 
#     p+=2
# print(su)


