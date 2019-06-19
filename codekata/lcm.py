def lcm(no1,no2):
  if no1>no2:
    a=no1
  else:
    a=no2
  while(True):
    if a%no1==0 and a%no2==0:
      l=a
      break
    a=a+1
  return l
  
no1,no2=map(int,input().split())
ans=lcm(no1,no2)
print(ans)
