num=int(input())
numlis=list(map(int,input().split()))
if len(numlis)==num:
  a=max(numlis)
  b=min(numlis)
  c=a-b
print(c)
