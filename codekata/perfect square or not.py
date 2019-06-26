num1,num2=map(int,input().split())
num=num1*num2
ans=0
while ans*ans<num:
  ans=ans+1
if ans*ans==num:
  print("yes")
else:
    print("no")
