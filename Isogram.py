s=str(input()).lower()
a=True
for i in range(0,len(s)):
    if s.count(s[i])>1:
        a=False
        print("No")
        break
if a:
    print("Yes")
