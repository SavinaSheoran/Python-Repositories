#functions
def greet():
    print("hello world")
greet()



def sum(a, b):
   c = a + b
   print(c)
sum(5, 6)




#checking number is even or odd
def check_num(num):
    if num % 2 == 0:
        return "even" 
    else:
        return "odd"
num = int(input("enter number: "))
print(f"entered {num} is {check_num(num)}")





#check largest among three
def check_largest_num(a, b, c):
    if a>=b and a>=c:
        return "a"
    elif b>=c and b>=a:
        return "b"
    else:
        return "c"
    
num1 = int(input("enter a: "))
num2 = int(input("enter b: "))
num3 = int(input("enter c: "))
max_num = check_largest_num(num1, num2, num3)
print(max_num)




#Factorial 
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n - 1)

# Example
num = int(input("Enter a number: "))
if num < 0:
    print("Factorial is not defined for negative numbers.")
else:
    print(f"The factorial of {num} is {factorial(num)}.")




#Reverse 
def reverse_string(text):
    reversed_text = ""
    for char in text:
        reversed_text = char + reversed_text
    return reversed_text
    
#example
input_str = input("enter a string: ")
print("reversed_string:", reverse_string(input_str))





#Fibonacci Series
def fibonacci(n):
    if n <= 0:
        return "Invalid input. Please enter a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Example usage
num = int(input("Enter the position (n) in Fibonacci sequence: "))
result = fibonacci(num)
print(f"The {num}th Fibonacci number is: {result}")