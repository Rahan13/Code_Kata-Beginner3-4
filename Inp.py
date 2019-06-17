s=[]
def getInput():
    while True:
        c=input().split()
        if len(c)!=0:
            s.append((abs(int(c[0])-int(c[1]))))
        else:
            break

getInput()
[print(i) for i in s]
