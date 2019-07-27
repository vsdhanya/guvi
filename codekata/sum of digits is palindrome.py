num=int(input())
sum=0
while(num!=0):
  rem=num%10
  sum=sum+(rem)
  num=num//10
sum=str(sum)
sum1=sum[::-1]
if sum==sum1:
  print("YES")
else:
  print("NO")
