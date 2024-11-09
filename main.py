import datetime
import locale
locale.setlocale(locale.LC_ALL, '')

year=input("Enter year: ")
month=input("Enter month: ")
year=int(year)
month=int(month)

date=datetime.datetime(year,month,1)

while True:
    if month != date.month:
        break
    day=date.strftime("%A")
    monthName=date.strftime("%B")
    print("{0}-{1} {2} ({3})".format(date.day,monthName,year,day))
    date=date+datetime.timedelta(days=1)