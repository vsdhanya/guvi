word=input()
count=0
for i in word:
  if i.isdigit()!=True and i.isalpha()!=True and i!=' ' :
    count=count+1
print(count)
