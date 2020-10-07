import calendar
year = int(input("Welcome to calendar printer please specyfy:(please use YYYY, then MM when asked)\nwhat year? : "))
month = int(input("what month? : "))
tc= calendar.TextCalendar(firstweekday=0)
print(tc.formatmonth(year, month))
#so fun :D
