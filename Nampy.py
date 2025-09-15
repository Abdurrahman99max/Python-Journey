# Create arrays: 1d array
import numpy as np

PLP_Array = np.array([1, 2, 3])
print(PLP_Array) # Output: [1 2 3 4 5]
# 2d array
PLP_Array2D = np.array([[1, 2, 3], [4, 5, 6]])
print(PLP_Array2D) # Output: [[1 2 3] [4 5 6]]

# Calculate the mean of the array
mean_value = np.mean(PLP_Array)
print("Mean value:", mean_value) # Output: Mean value: 3.5

# Calculate the area of a triangle
def triangle_area(base, height):
    return 0.5 * base * height
area = triangle_area(5, 10)
print("Area of the triangle:", area) # Output: Area of the triangle: 25.0

# Calculate the factorial of a number
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)
fact_5 = factorial(5)
print("Factorial of 5:", fact_5) # Output: Factorial of 5: 120

# Calculate the Fibonacci sequence up to n terms
def fibonacci(n):
    fib_sequence = [0, 1]
    while len(fib_sequence) < n:
        next_value = fib_sequence[-1] + fib_sequence[-2]
        fib_sequence.append(next_value)
    return fib_sequence[:n]
fib_10 = fibonacci(10)
print("Fibonacci sequence up to 10 terms:", fib_10) # Output: Fibonacci sequence up to 10 terms: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
