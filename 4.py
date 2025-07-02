#while loop


i = 1
while i<11:
    print(i)
    i +=1



# Print all even numbers from 1 to 50 using a while loop

i = 1
while i <= 50:
    if i % 2 == 0:
        print(i)
    i += 1

#Print sum of 1 to 100
i = 1
total = 0
while i <= 100:
    total += i 
    i += 1

print("sum of 1 to 100:", total)


# Print the multiplication table of a number using a while loop

num = int(input("Enter a number: "))
i = 1

print(f"Multiplication table of {num}:")
while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1



#Factorial using While Loop
num = int(input("enter number: "))
factorial = 1
i = 1
while i < num:
    factorial *= i
    i += 1
print(f"Factorial of {num} is {factorial}")



# Keep taking numbers until user enters 0, then print the total sum

total = 0

while True:
    num = int(input("Enter a number (0 to stop): "))
    if num == 0:
        break
    total += num

print("Total sum is:", total)


# Keep asking for the correct password

correct_password = "python123"

while True:
    entered_password = input("Enter the password: ")
    
    if entered_password == correct_password:
        print("Access granted ✅")
        break
    else:
        print("Incorrect password. Try again ❌")




# Print a number triangle using a while loop

rows = 5
i = 1

while i <= rows:
    j = 1
    while j <= i:
        print(j, end=' ')
        j += 1
    print()  # Move to the next line after each row
    i += 1


# ATM PIN system with 3 incorrect attempts allowed

correct_pin = "1234"
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    entered_pin = input("Enter your ATM PIN: ")
    
    if entered_pin == correct_pin:
        print("✅ Access granted. Welcome!")
        break
    else:
        attempts += 1
        print(f"❌ Incorrect PIN. Attempts left: {max_attempts - attempts}")

if attempts == max_attempts:
    print("🚫 Card blocked due to too many incorrect attempts.")
