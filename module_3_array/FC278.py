## anagram 
st1=list(input("enter word >> "))
st2=list(input("enter word >> "))
c1=0
for i in st1:
    c1+=1
c2=0
for j in st2:
    c2+=1
count=0
if c1!=c2:
    print("Not Anagram ")
else:
    if c1 == c2:
        for k in range(c1):
            for l in range(c2):
                if st1[k] == st2[l] :
                    count+=1
        print("Anagram ")
    else:
        print("Not Anagram")


