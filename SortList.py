n =int(input())
a =input().split()
c =list(map(int,a))
c = sorted(c)
mid = int(n/2)
print(c[mid])
