#  ***************************Question 4************************

# Q4. The power of one line -
# Given a dictionary, switch position of key and values in the dict, i.e., value becomes the key and
# key becomes value. The function's body shouldn't have more than one statement.
# f({
# "key1": "value1",
# "key2": "value2",
# "key3": "value3",
# "key4": "value4",
# "key5": "value5"
# }) should return
# {
# "value1": "key1",
# "value2": "key2",
# "value3": "key3",
# "value4": "key4",
# "value5": "key5"
# }

#Code

def f(dict):
    return {value: key for key, value in dict.items()}



n = int(input("Enter the size of dictionary: "))
dict = {}
for i in range(n):
    key = (input("Enter the key: "))
    value = (input("Enter the value: "))
    dict[key] = value

print(f(dict))