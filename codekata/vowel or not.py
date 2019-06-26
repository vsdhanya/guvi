alpha=input()
c=0
vowels=['a','A','e','E','i','I','o','O','u','U']
for i in alpha:
    if i in vowels:
      c=0
      print("yes")
      break
    else:
      c=c+1
if c!=0:
  print("no")
