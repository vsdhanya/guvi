num=int(input())
if num<=2:
  print("0")
elif num>2:
  for i in range(2,num):
    if i>1:
      for j in range(2,i):
        if(i%j==0):
          break
      else:
        print(i,end=" ")
    else:
      break
