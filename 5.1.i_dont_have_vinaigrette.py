import datetime
from datetime import datetime
import random


def get_date():
    date = input("Enter a date: ")
    try:
        # %Y - checks if the year is in the format YYYY
        date = datetime.strptime(date, '%Y-%m-%d')
        return date
    except Exception as e:
        print(e)
        exit()


def get_random_date_in_middle(date1, date2):
    epoch1 = date1.timestamp()
    epoch2 = date2.timestamp()
    start, end = (epoch1, epoch2) if (epoch1 < epoch2) else (epoch2, epoch1)
    rand_epoch = random.randint(start, end)
    return datetime.fromtimestamp(rand_epoch)


def check_day(date, day):
    return date.strftime("%A") == day


date1 = get_date()
date2 = get_date()
rand_date = get_random_date_in_middle(date1, date2)
print(rand_date.strftime('%Y-%m-%d'))
if check_day(rand_date, 'Monday'):
    print("I don't have a vinaigrette!")
