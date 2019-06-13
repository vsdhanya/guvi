number=int(input())
t=number
sum=0
while(number>0):
  remain=number%10
  sum=sum+(remain**3)
  number=number//10
if sum==t:
  print("yes")
else:
  print("no")
