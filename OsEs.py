s=str(input())
os=""
es=""
for i in range(0,len(s)):
    if(i%2==0):
        es=es+s[i]
    else:
        os=os+s[i]
print(es,os)
