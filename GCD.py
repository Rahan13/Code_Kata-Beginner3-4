s=input().split()
s=list(map(int,s))
m=1
for i in range(1,min(s)+1):
    if s[0]%i==0 and s[1]%i==0:
        m=i
print(m)
