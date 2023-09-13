n=int(input("enter row >>>> "))
for i in range(1,n+1):
    s=''
    for j in range(n-i,0,-1):
        s+=' '
    
    for k in range(i):
        s+="*"
    print(s)


