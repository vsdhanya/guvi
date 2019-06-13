numb1,numb2=map(int,input().split())
for i in range(numb1+1,numb2):
  a=len(str(i))
  t=i
  sum1=0
  while(i>0):
    remain=i%10
    sum1=sum1+(remain**a)
    i=i//10
  if sum1==t:
    print(sum1)
  
