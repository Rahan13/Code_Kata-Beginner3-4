n=input().split()
n = "".join(n)
cnum=0
anum=0
for i in range(0,len(n)):
    if n[i].isnumeric():
        cnum+=1
        continue
    elif n[i].isalpha():
        anum+=1
        continue
if(anum>0 and cnum>0):
    print("yes")
else:
    print("no")
