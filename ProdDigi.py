s=int(input())
prod=1
while(s>0):
    prod=prod*(s%10)
    s=int(s/10)
print(prod)
