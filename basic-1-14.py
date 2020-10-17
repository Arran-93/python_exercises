import datetime
day1= (2014,7,2)
day2= (2014,7,11)
(y1,m1,d1)= day1
day1=datetime.datetime(y1,m1,d1)
(y2,m2,d2)= day2
day2=datetime.datetime(y2,m2,d2)
print(int(day2.strftime('%j'))-int(day1.strftime('%j')))
