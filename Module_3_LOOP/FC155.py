## pattern of D  
n=int(input("enter n >>>"))
for i in range(1,n+1):
    s=''
    for j in range(n+1):
        if i == 1:
            s+='*'
            if i==n:
                s+='*'
        elif i == n:
            s+='*'
        else:
            if j==1:
                s+='*'
            elif j==n:
                s+=' *'
            else:
                s+=' '
    print(s) 





