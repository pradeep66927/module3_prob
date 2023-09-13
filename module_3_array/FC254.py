# ##transpose matrix a to other matrix 
a=[[2,1,4],
   [7,5,6]]
b=[[0,0],
   [0,0],
   [0,0]]
for i in a:
    print(i)

for j in range(2):
    for k in range(3):
        b[k][j]=a[j][k]
for l in b:
    print(l) 


