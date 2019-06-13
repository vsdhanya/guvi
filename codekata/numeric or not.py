number=input()
if any(a.isalpha() for a in number):
  print("No")
elif any(a.isdigit() for a in number):
  print("yes")
