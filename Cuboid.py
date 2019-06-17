s=input().split()
s=list(map(int,s))
sa=2*(s[0]*s[1]+s[1]*s[2]+s[2]*s[0])
vol=s[0]*s[1]*s[2]
print(sa,vol)
