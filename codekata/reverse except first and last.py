st=input().split()
print(st[0],end=" ")
for i in range(1,len(st)-1):
  print(st[i][::-1],end=" ")
print(st[len(st)-1])
