num=int(input())
sum=0
while(num!=0):
  rem=num%10
  sum=sum+(rem**2)
  num=num//10
print(sum)
