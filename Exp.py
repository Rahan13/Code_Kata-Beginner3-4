n=int(input())
a=True
if(n%2==0):
    for i in range(0,20):
        if n==2**i:
            a=False
            print("yes")
            break
    if a:
        print("no")
else:
    print("no")
