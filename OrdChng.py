n=input()
s=input().split()
for i in range(0,len(s)-1):
    if int(s[i]) > int(s[i+1]):
        print(i)
        break
print("")
