number=int(input())
numlist=list(map(int,input().split()))
if(number==len(numlist)):
  numlist.sort()
  for i in numlist:
    print(i,end=" ")
