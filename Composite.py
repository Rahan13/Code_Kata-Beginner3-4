s=int(input())
count=0
for i in range(1,s+1):
    if s%i==0:
        count+=1
    if count>2:
        print("yes")
        break
if count==2:
    print("no")
