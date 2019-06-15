n=int(input())
b=list()
while(n>0):
    b.append(n%10)
    n=int(n/10)
i=len(b)-1
while(i>=0):
    print(b[i],end=" ")
    i-=1
