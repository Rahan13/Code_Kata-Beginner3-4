n=input().split()
s=input().split()
k=int(n[1])
while(k>1):
  mini=min(s)
  s.remove(mini)
  k-=1
print(min(s))
