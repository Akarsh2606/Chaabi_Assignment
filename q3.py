#  ***************************Question 3************************

# Q3. Column Sorting, yay!

# Given a list of dicts, write a program to sort the list according to a key given in input.

#Code

def column_sort(list, key):
    arr = sorted(list, key = lambda x: x[key])
    return arr


list = [
    {"fruit": "orange", "color": "orange"},
    {"fruit": "apple", "color": "red"},
    {"fruit": "banana", "color": "yellow"},
    {"fruit": "blueberry", "color": "blue"}
]
ans = column_sort(list, "fruit")
print(ans)

ans = column_sort(list, "color")
print(ans)