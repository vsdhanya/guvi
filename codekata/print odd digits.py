number=list(input())
lis=[]
for i in number:
  if int(i)%2!=0:
    lis.append(i)
for i in lis:
  print(i,end=" ")
