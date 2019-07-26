n1=int(input())
inp=input().split()
if len(inp)==n1:  
  st=inp[::-1]
  for i in range(n1-1):
    print(st[i]+'->',end="")
  print(st[n1-1])
