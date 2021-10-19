import sys

day_number = sys.argv[1]
if int(day_number):
    day_number = int(day_number)
    if day_number <= 7:
        print('1')
    else:
        week_number = (day_number // 7)
        print(week_number)
else:
    print('wrong input (not int)')