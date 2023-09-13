## binary search through find a number 

n=int(input("enter term >> "))
l=[0]*n
for i in range(n):
    num=int(input("enter the num >> "))
    l[i]=num
for j in range(n):
    for k in range(n-1-j):
        if l[k] > l[k+1]:
            l[k],l[k+1] = l[k+1],[k]
print(l)
search=int(input("enter ther number to search >> "))

left, right = 0,n - 1

while left <= right:
    mid = left + (right - left) // 2 
    
    if l[mid] == search:
        print(f"Element {search} found at index {mid}")
        break
    elif l[mid] < search:
        left = mid + 1
    else:
        right = mid - 1
else:
    print(f"Element {search} not found in the list")
