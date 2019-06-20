numb=int(input())
fact=1
if numb==0 or numb==1:
  print(1)
else:
  for i in range(1,numb+1):
    fact=fact*i
  print(fact)
