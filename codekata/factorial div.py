numb,numb1=map(int,input().split())
fact=1
fac=1
if numb==0 or numb==1 or numb1==0 or numb1==1:
  print(1)
else:
  for i in range(1,numb+1):
    fact=fact*i
  for j in range(1,numb1+1):
    fac=fac*j
  ans=int(fact/fac)
  print(ans)
