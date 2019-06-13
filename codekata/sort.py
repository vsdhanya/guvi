given_no=int(input())
numlis=list(map(int,input().split()))
if(given_no==len(numlis)):
  numlis.sort()
  for i in numlis:
    print(i,end=" ")
