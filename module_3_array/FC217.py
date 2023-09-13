# a=[1,2,3,4,5,6,7,8,9,10]
# i=1
# ev=0
# od=0
# while i<10:
#     if i%2==0:
#         if a[i-1]%2==0:
#             ev+=a[i-1]
#     else:
#         if a[i-1]%2==1:
#             od+=a[i-1]
#     i+=1
# print(ev)
# print(od)

## add odd position and even position number input taken by user 
n=10
l=[0]*n
for i in range(n):
    n1=int(input("enter num >>> "))
    l[i]=n1
print(l)
su_odd_positions =0
su_even_positions=0
for j in range(n):
    if j % 2 == 0:
        su_even_positions+=l[j] 
    else:
        su_odd_positions+=l[j]
print(su_even_positions)
print(su_odd_positions)
