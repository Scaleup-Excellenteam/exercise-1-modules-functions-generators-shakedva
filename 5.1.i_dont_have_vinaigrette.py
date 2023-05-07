import datetime
from datetime import datetime
import random

MESSAGE = "I don't have a vinaigrette!"
MONDAY = "Monday"
DATE_FORMAT = '%Y-%m-%d'
DAY_FORMAT = "%A"


def get_date():
    """
    :return: a datetime date
    """
    while True:
        date = input("Enter a date in the format YYYY-MM-DD: ")
        try:
            # %Y - checks if the year is in the format YYYY
            date = datetime.strptime(date, DATE_FORMAT)
            return date
        except ValueError as ve:
            print(f"The date '{date}' does not match the format YYYY-MM-DD. Please enter a new date.")


def get_random_date_in_middle(start_date, end_date):
    """
    :param start_date: datetime date
    :param end_date: datetime date
    :return: a datetime date between both dates
    """
    start_date_timestamp = start_date.timestamp()
    end_date_timestamp = end_date.timestamp()
    if end_date_timestamp < start_date_timestamp:
        start_date_timestamp, end_date_timestamp = end_date_timestamp, start_date_timestamp
    timestamp_between = random.randint(start_date_timestamp, end_date_timestamp)
    return datetime.fromtimestamp(timestamp_between)


def check_day(date, day):
    """
    :param date: datetime date
    :param day:  str representation of a day
    :return: True if the @param date's day is equal to @param day
    """
    return date.strftime(DAY_FORMAT) == day


def main():
    """
    Receives two dates from the user in format YYYY-MM-DD.
    It generates a random date in between those dates.
    Prints MSG if the generated date is on monday.
    """
    start_date = get_date()
    end_date = get_date()
    date_between = get_random_date_in_middle(start_date, end_date)
    print(date_between.strftime(DATE_FORMAT))
    if check_day(date_between, MONDAY):
        print(MESSAGE)


if __name__ == "__main__":
    main()
