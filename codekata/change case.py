st=input()
for i in st:
  if i.isupper()==True:
    print(i.lower(),end="")
  if i.islower()==True:
    print(i.upper(),end="")
