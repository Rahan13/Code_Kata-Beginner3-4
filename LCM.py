s=input().split()
s=list(map(int,s))
m=[]
i=2
while(i<=max(s)):
    if s[0]%i==0 and s[1]%i==0:
        s[0]=int(s[0]/i)
        s[1]=int(s[1]/i)
        m.append(i)
        i=2
        continue
    if s[0]%i==0:
        s[0]=int(s[0]/i)
        m.append(i)
    if s[1]%i==0:
        s[1]=int(s[1]/i)
        m.append(i)
    if s[0]==1 and s[1]==1:
        break
    i+=1
prod=1
for i in m:
    prod*=i
print(prod)
