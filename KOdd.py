s=input().split()
nums=input().split()
nums=list(map(int,nums))
k=1
for i in range(0,int(s[0])):
  if nums[i]%2 != 0:
    if k==int(s[1]):
      print(nums[i])
      break
    else:
      k+=1
