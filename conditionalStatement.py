#Conditional Satetments (if-else statements)
a = int(input("Enter age:"))
if(a>18):
  print("you can drive")
  print("yes")
else:
  print("you cannot drive")
  print("no")
print("i'm happy now")

applePrice = 10
budget = 200
if (budget - applePrice < 50):
  print("Alexa, add 1kg Apples to the cart.")
else:
  print("Alexa, do not add Apples to the cart.")
num = int(input("enter the value of num : "))

#if-elif-else
if (num < 0):
  print("number is negative.")
elif(num == 0):
  print("number is zero.")
elif(num == 999):
  print("number is special")
else:
  print("number is positive.")

num = int(input("enter the value of num : "))
if(num < 0):
  print("number is neagtive")
elif(num > 0):
  if(num <= 10):
    print("number is between 1-10")
  elif(num > 10 and num <=20):
    print("number is between 11-20")
  else:
    print("number is greater than 20")
else:
  print("number is zero")

#Time Module (Internal python Module)
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
s = int(time.strftime('%S'))
if(s < 12):
  print("good morning")
elif(s>12 and s<17):
  print("good afternoon")
else:
  print("good night")