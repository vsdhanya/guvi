word=input()
let=False
num=False
for i in word:
  if i.isalpha():
    let=True
  if i.isdigit():
    num=True
if num==True and let==True:
  print("Yes")
else:
  print("No")
