## Diagonal matrix 
m1=[[1,0,0],[0,1,0],[0,0,1]]
# m1=[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]
# want to check 4X4 matrix then change loop range and uncomment this above line 
c=0
for i in m1:
    for j in i:
        c+=1
if c % (c**0.5) == 0:
    I_matrix= True
    for k in range(3):
        for l in range(3):
            if k == l:
                if m1[k][l] ==0 :
                    I_matrix=False
                    break
            else:
                if m1[k][l] !=0:
                    I_matrix=False
                    break
    if I_matrix:
            print("Diagonal matrix")
    else:
        print("Not Diagonal matrix")
else:
    print("Not Diagonal matrix")

