## Duplicate array in list given by user
n=int(input("no of element in array >> "))

l=[0]*n
for i in range(n):
    ele=int(input("enter ele >> "))
    l[i]=ele
dup_ele=False
for j in range(n):
    for k in range(j+1,n):
        if l[j] == l[k]:
            dup_ele=True
            print("duplicate:",l[j])
if dup_ele == False:
    print("No duplicate Found ")

