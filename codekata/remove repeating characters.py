w=list(input())
l=[]
for i in w:
  if i not in l:
    l.append(i)
for i in l:
  print(i,end="")
