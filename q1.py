#  ***************************Question 1************************

# Get your basics right - Implement selection sort algorithm in python. The function accepts a
# list in the input and returns a sorted list.
# E.g.
# Input f1([5,416,54,21,6135,15,741]) should
# Return [5, 15, 21, 54, 416, 741, 6135]


# Code

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        temp = arr[i]
        arr[i] = arr[min_idx]
        arr[min_idx] = temp
    
    return arr



list = []
n = int(input("Enter number of elements: "))

for i in range(0, n):
    element = int(input())
    list.append(element) 

ans = selection_sort(list)
print(ans)
