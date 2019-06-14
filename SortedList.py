n =int(input())
a =input().split()
b =list(map(int,a))
b = sorted(b)
[print(i, end=" ") for i in b]
