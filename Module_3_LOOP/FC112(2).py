###  triangle of 4 row * should be increase 2*i+1
n=int(input("enter row >>>> "))
for i in range(0,n):
    s=''
    for j in range(n-i-1):
        s+=' '

    for k in range(2*i+1):
        s+="*"
    print(s)


