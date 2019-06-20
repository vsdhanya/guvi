no=int(input())
fact=1
if no==0 or no==1:
  print(1)
else:
  for i in range(1,no+1):
    fact=fact*i
  print(fact)
