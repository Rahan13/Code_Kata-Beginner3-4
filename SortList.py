n =int(input())
a =input().split()
c =list(map(int,a))
c = sorted(c)
[print(d, end=" ") for d in c]
