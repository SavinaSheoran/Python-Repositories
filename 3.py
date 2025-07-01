#For Loop Questions


for i in range(1, 11):
    print(i)



for i in range(1, 51):
    if(i%2==0):
      print(i)
    else:
       print("None")



number = int(input("enter number:"))
for i in range(1, 11):
   product = number*i
   print(product)



total = 0
for i in range(1, 101):
    total += i

print("sum of 1 to 100:", total)



square = 0
for i in range(1, 11):
    print(f"square of {i} is {i**2}")



list1 = (1, "Apple", 2, "Banana", "Harry", 4)
for i in list1:
    print(i)



str1 = input("enter a string: ")
vowels = "aeiouAEIOU"
count = 0
for char in str1:
    if char in vowels:
        count += 1
    
print("vowels in str1:", count)



text = input("enter a string: ")
reversed_text = ""

for char in text:
    reversed_text = char + reversed_text

print("Reversed string:", reversed_text)



#Factorial
number = int(input("Enter number: "))
fact = 1

for  i in range(1, number+1):
    fact = fact *i

print(fact)



#Fibonacci Series
#Print Fibonacci series up to n terms

n = int(input("Enter the number of terms: "))

a, b = 0, 1  # First two terms

if n <= 0:
    print("Please enter a positive number.")
elif n == 1:
    print("Fibonacci sequence up to 1 term:")
    print(a)
else:
    print(f"Fibonacci sequence up to {n} terms:")
    print(a, b, end=' ')
    for _ in range(2, n):
        c = a + b
        print(c, end=' ')
        a, b = b, c
