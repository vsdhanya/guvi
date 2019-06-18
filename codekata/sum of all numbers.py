numb=int(input())
numlis=list(input().split())
sum=0
if len(numlis)==numb:
  for i in numlis:
    sum=sum+int(i)
  print(sum)
