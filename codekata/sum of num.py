num,num1=map(int,input().split())
list1=list(map(int,input().split()))
sum_num=0
if(len(list1)==num):
  for i in range(len(list1)+1):
    if i<num1:
      sum_num+=list1[i]
  print(sum_num)
