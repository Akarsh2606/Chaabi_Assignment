#  ***************************Question 10************************

# Q10. Of date and days
# Write a func that takes 2 args:
# date - string representing a date in the form of 'yy-mm-dd'
# n - integer
# Returns the string representation of date n days before 'date'
# E.g. f('16-12-10', 11) should return '16-11-29'

#Code

from datetime import datetime, timedelta

def get_date(date, n):
    date_convert = datetime.strptime(date, '%y-%m-%d')
    new_date = date_convert - timedelta(days = n)
    new_date_str = new_date.strftime('%y-%m-%d')
    return new_date_str


date = input("Enter the date: ")
n = int(input("Enter the days: "))

ans = get_date(date , n)
print(ans)