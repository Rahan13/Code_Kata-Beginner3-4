n =input()
sc = '".[@_!#$%^&*()<>?/\|}{~:]'
count=0
for i in range(0,len(n)):
    if n[i] in sc:
        count +=1
print(count)
