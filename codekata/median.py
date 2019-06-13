num=int(input())
numli=list(map(int,input().split()))
if(num==len(numli)):
  numli.sort()
  med=num//2
print(numli[med])
