hour1,minute1=map(int,input().split())
hour2,minute2=map(int,input().split())
hr=abs(hour1-hour2)
mins=abs(minute1-minute2)
print(hr,mins)
