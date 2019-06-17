s=[]
c=input()
if len(c)!=0:
  if "%" in c:
    nums=c.split("%")
    nums=list(map(int,nums))
    s.append(nums[0]%nums[1])
  else:
    nums=c.split("/")
    nums=list(map(int,nums))
    s.append(int(nums[0]/nums[1]))
[print(val) for val in s]
