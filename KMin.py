s=input().split()
k=int(s[1])
while(k>1):
  mini=min(s)
  s.remove(mini)
  k-=1
print(min(s))
