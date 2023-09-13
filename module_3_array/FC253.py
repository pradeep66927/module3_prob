## Multiply two array matrix and store in seprate matrix 
a=[[2,3,4],
   [7,7,1],
   [3,4,7]]
b=[[1,2,6],
   [2,1,3],
   [3,1,4]]
c=[[0,0,0],
   [0,0,0],
   [0,0,0]] 
for i in range(3):
    for j in range(3):
        c[i][j]=a[i][j]*b[i][j]
for k in c:
    print(k)