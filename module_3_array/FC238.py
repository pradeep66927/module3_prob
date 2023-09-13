## selection sort  , insertion sort , bubble sort 
## 2. Insertion sort 


## 3 Bubble sort 
n=[8,3,8,1,4,3,7,3]
c1=0
for c in n:
    c1+=1
for m in range(c1):
    for p in range(c1-1-m):
        if n[p] > n[p+1]:
            # t=n[p]
            # n[p]=n[p+1]
            # n[p+1]=t
            n[p],n[p+1]=n[p+1],n[p]
print(n)
