n=int(input())
sum=0
num=input().split()
if(len(num)==n):
  for i in num:
    if int(i)<0:
      sum=sum+int(i)
    else:
      break
  print(sum)
