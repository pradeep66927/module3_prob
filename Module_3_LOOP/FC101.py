# ## Reverse the number which given by user 
# n=int(input("enter no: "))
# str_n=str(n)
# print(int(str_n[: : -1]))

n=int(input("enter num >>> "))
rev_d=''
while n !=0:
    d=n % 10
    rev_d+=str(d)
    n=n//10
print(rev_d)

