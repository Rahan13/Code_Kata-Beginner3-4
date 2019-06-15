n=int(input())
count=0
while(n>0):
    count+=int(n%10)
    n=int(n/10)
print(count)
