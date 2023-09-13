## sum should be 12 from given  element 7,5 etc

arr=[3,6,7,5,10]
arr2=[0]*1
c=0
k=12
for i in range(4):
    if arr[i] + arr[i+1] == 12:
        arr2[c]=arr[i],arr[i+1]
print(*arr2)
