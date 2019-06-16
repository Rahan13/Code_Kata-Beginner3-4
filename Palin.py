a=input().lower()
b=""
i=len(a)-1
while(i>=0):
    b += a[i]
    i-=1
if a==b:
    print("yes")
else:
    print("no")
