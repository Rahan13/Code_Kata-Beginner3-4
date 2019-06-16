a=input().lower()
b="aeiou"
c=True
for i in range(0,len(a)):
    if a[i] in b:
        c=False
        print("yes")
        break
if c:
    print("no")
