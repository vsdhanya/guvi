st=input()
k=[]
for i in st:
  if i.isnumeric():
    k.append(i)
print("".join(k))
