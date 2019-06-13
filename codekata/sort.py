number=int(input())
numlis=list(map(int,input().split()))
numlis.sort()
for i in numlis:
  print(i,end=" ")
