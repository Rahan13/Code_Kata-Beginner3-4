n =int(input())
a=1
b=0
for i in range(0,n):
   c=a+b
   print(c,end=" ")
   a=b
   b=c
