s=input().split()
val=int(s[0])*int(s[1])
val=val**0.5
if val%int(val)==0:
    print("yes")
else:
    print("no")
