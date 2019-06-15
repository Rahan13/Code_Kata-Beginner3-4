bin = input()
b="01"
a=True
for i in range(0,len(bin)):
    if bin[i] in b:
        continue
    else:
        a=False
        print("no")
        break
if a:
    print("yes")
