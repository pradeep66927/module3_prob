## Number decimal to binary 
dec=int(input("enter decimal number >>> "))
st=''
while dec > 0:
    r=dec % 2
    st=str(r)+ st
    dec = dec//2
print(st)

