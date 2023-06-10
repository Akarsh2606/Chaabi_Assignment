#  ***************************Question 6************************

# Q6. Every other sub-list
# Given a list and 2 indices as input, return the sub-list enclosed within these 2 indices. It should
# contain every second element.
# E.g.
# Input f([2,3,5,7,11,13,17,19,23,29,31,37,41], 2, 9)
# Return [5, 11, 17, 23]

#Code

def f(list , st , end):
    ans = []
    for x in range(st , end , 2):
        ans.append(list[x])
    return ans

n = int(input("Enter the size of list: "))
list = []
for i in range(n):
    data = input("Enter the data: ")
    list.append(data)

start_index = int(input("Enter the start index: "))
end_index = int(input("Enter the end index: "))
print(f(list , start_index , end_index + 1))