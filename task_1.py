#task 1

first = int(input("Input first number: "))
second = int(input("Input second number: "))
third = int(input("Input third number: "))

maximum = max(first, second, third)
minimum = min(first, second, third)
remainder = ((first + second + third) - maximum - minimum)

print("Maximum: ", maximum)
print("Minimum: ", minimum)
print("Remainder: ", remainder)
print("Remainder: ", remainder)
