## find the positions of the element in array or matrix 
m=[[2,3,9],
   [6,7,1],
   [8,4,5]]
n=int(input('enter user >> '))
for i in range(3):
    for j in range(3):
        if n == m[i][j]:
            print([i],[j])
            

