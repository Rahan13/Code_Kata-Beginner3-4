n=int(input())
a=input().split()
a=list(map(int,a))
if a[0]<n and a[1]>n:
    print("yes")
else:
    print("no")
