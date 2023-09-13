## number of list move one index forword to its original place and last ele will be at first
l= [1, 2, 3, 4, 5]
c=0
for i in l:
    c+=1

t = l[c - 1] 

for j in range(c - 1, 0, -1):
    l[j] = l[j - 1]  

l[0] = t

print("rotated list:", l)
