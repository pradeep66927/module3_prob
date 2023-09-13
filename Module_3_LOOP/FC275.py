## twisted prime reverse of digit is also prime 
n=int(input("enter nuber>> "))
st_n=str(n)
c=0
for i in st_n:
    c+=1
r_p=''
for i in range((c-1),-1,-1):
    r_p+=st_n[i]
count=0
for i in range(1,int(r_p)+1):
    if int(r_p) % i == 0:
        count+=1 
if count == 2:
    print("twisted prime ")
else :
    print("not twisted prime")

