# ## check jumbled number if neighour max difference is 1
n=input("enter no>> ")
c=0
for digit in n:
    c+=1
is_jumb=True
for i in range(c-1):
    d=int(n[i])-int(n[i+1])
    if d < 0:
        d=-d
    if d>1:
        is_jumb=False 
        break
if is_jumb:
    print("True")
else:
    print("false")


