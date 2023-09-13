## parallelogram type pattern 
n=int(input(" enter row >> "))
for i in range(0,n):
    s=''
    for j in range(n-i-1):
        s+=' '

    for k in range(2*i+1):
        s+="*"
    print(s)
for l in range(n-2,-1,-1):
    s=''
    for m in range(n-l-1):
        s+=' '
    for p in range(2*l+1):
        s+="*"
    print(s)



# n=int(input("enter row >>> "))
# for i in range(1,n+1):
#     a=''
#     for j in range(n-i):
#         a+=' '
#     b=''
#     for k in range(i):
#         b+='*'
#     print(a,b)
    
# n=int(input('enter value >>'))
# i=1
# while i<=n:
#     a=''
#     j=n-i
#     while j>0:
#         a+=' '
#         j-=1
#     k=i
#     b=''
#     while k>=1:
#         b+='*'
#         k-=1
#     print(a,b)    
#     i+=1
