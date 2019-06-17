s=int(input())
num=0
while(s>0):
    num=num*10+(s%10)
    s=int(s/10)
print(num)
