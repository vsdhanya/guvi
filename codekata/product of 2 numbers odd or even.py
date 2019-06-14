numb1,numb2=map(int,input().split())
prod=numb1*numb2
if prod>0:
  if prod%2==0:
    print("even")
  else:
    print("odd")
