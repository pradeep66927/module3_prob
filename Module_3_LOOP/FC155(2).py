## hollow triangle 
n=int(input("enter n >> "))
for i in range(1,n+1):
    s=''
    for j in range(1,i+1):
        if i < 3:
            s+='*'
        if i == n:
            s+="*"
        
        if i < n:
            if i > 2:
                if j == 1:
                    s+='*'
                elif i==j:
                    s+='*'
                else:
                    s+=' '
    print(s)
                

# 2)
# n=int(input('enter value >>'))
# i=1
# while i<=n:
#     j=1
#     a=''
#     while j<=i:
#         if (i<3):
#             a+='*'
#         if i==n:
#             a+='*'
#         if i<n:
#             if i>2:
#                 if j==1:
#                     a+='*'
#                 elif i==j:
#                     a+='*'
#                 else:
#                     a+=' '
#         j+=1
#     print(a)
#     i+=1