num,a,d=map(int,input().split())
sum1=0
for i in range(1,num+1):
  sum=a+((i-1)*d)
  sum1=sum1+sum   
print(sum1)
