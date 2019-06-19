def gcd(no1,no2):
  if no1==0:
    return no2
  if no2==0:
    return no1
  else:
    return gcd(no2,no1%no2)
no1,no2=map(int,input().split())
ans=gcd(no1,no2)
print(ans)
