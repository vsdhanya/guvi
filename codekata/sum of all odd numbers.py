n1,n2=map(int,input().split())
sum=0
for i in range(n1,n2+1):
  if i%2!=0:
    sum=sum+int(i)
print(sum)
