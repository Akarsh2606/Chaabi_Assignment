#  ***************************Question 9************************

# Q9.
# Write a func that takes 3 args:
# from_date - string representing a date in the form of 'yy-mm-dd'
# to_date - string representing a date in the form of 'yy-mm-dd'
# difference - int
# Returns True if from_date and to_date are less than difference days away from each other, else
# returns False.

#Code

from datetime import datetime, timedelta

def check(from_date, to_date, diff):
    from_date = datetime.strptime(from_date, '%y-%m-%d')
    to_date = datetime.strptime(to_date, '%y-%m-%d')
    date_diff = to_date - from_date
    if date_diff < timedelta(days = diff):
        return True
    else:
        return False


from_date = input("Enter the from date: ")
to_date = input("Enter the to date: ")
diff = int(input("Enter the difference: "))
if(check(from_date , to_date , diff)):
    print(True)
else:
    print(False)