#  ***************************Question 7************************

# Q7. Calculate the factorial of a number using lambda function.

#Code

factorial = lambda n: 1 if n == 0 else n * factorial(n - 1)


n = int(input("Enter the number: "))
ans = factorial(n)
print("Factorial of", n, "is", ans)