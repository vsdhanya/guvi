numb=int(input())
f=1
s=1
print(f,s,end=" ")
if numb>0:
  for i in range(2,numb):
    next=f+s
    print(next,end=" ")
    f=s
    s=next
