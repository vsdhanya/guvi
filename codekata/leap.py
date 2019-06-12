leap=int(input())
if leap%4==0 and leap%100!=0:
  print ("yes")
elif leap%400==0:
  print("yes")
else:
  print("no")
