#  ***************************Question 11************************

# Q11. Something fishy there -
# Find output of following:
# def f(x,l=[]):
#   for i in range(x):
#       l.append(i*i)
#   print(l)

# f(2)
# f(3,[3,2,1])
# f(3)

#Answer

f(2) = [0 , 1]
f(3,[3,2,1]) = [3 , 2 , 1 , 0 , 1 , 4]
f(3) = [0 , 1 , 0 , 1 , 4]

# The third function call f(3) does not provide a value for l, so the default list from the first function call f(2) is used.