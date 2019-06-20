no=input()
if any(a.isalpha() for a in no):
  print("no")
elif any(a.isdigit() for a in no):
  print("yes")
