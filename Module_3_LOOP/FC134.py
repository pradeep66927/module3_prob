## pattern of triangle increasing then decreasing 
n=int(input("enter term >> "))
for i in range(n+1):
    s=""
    for j in range(i):
        s+="*"
    print(s)
for k in range(n-1 ,0,-1):
    s2=""
    for l in range(k):
        s2+='*' 
    print(s2)

