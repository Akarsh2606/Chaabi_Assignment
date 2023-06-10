#  ***************************Question 5************************

# Q5. Common, Not Common
# Given 2 lists in input. Write a program to return the elements, which are common to both
# lists(set intersection) and those which are not common(set symmetric difference) between the
# lists.
# Input:
# Mainstream = ["One Punch Man","Attack On Titan","One Piece","Sword
# Art Online","Bleach","Dragon Ball Z","One Piece"]
# must_watch = ["Full Metal Alchemist","Code Geass","Death
# Note","Stein's Gate","The Devil is a Part Timer!","One Piece","Attack
# On Titan"]
# f(mainstream, must_watch) should return:
# ["One Piece", "Attack On Titan"], ["Dragon Ball Z", "Death Note",
# "One Punch Man", "Stein's Gate", "The Devil is a Part Timer!", "Sword
# Art Online","Full Metal Alchemist","'Bleach", "Code Geass"]

#Code

def f(mainstream , must_watch):
    common = set(mainstream) & set(must_watch)
    non_common = set(mainstream) ^ set(must_watch)
    return common, non_common

n = int(input("Enter the size of main stream: "))
mainstream = []
for i in range(n):
    series = input("Enter the main stream: ")
    mainstream.append(series)

m = int(input("Enter the size of must watch: "))
must_watch = []
for i in range(m):
    series = input("Enter the must watch: ")
    must_watch.append(series)

print(f(mainstream , must_watch))