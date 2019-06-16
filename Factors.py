s=int(input())
b=list()
for i in range(1,s+1):
    if s%i==0:
        b.append(i)
    
[print(i,end=" ") for i in b]
