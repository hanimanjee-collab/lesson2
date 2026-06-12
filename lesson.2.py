#part1
city=input("write your city name")
temp=float(input("enter today's temp (in celsius"))

#part2
if temp>35:
    print("SCORCHING HOT!")
elif temp>25:
    print("WARM AND SUNNY!")
elif temp>15:
    print("COOL AND BREEZY!")
else:
    print("COLD! STAY WARM!")

#part3
import datetime
import calendar
current=datetime.datetime.now()
print("city:",city)
print("time now:",current)
print(calendar.calendar(current.year))