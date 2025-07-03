#Built-in Data Types


# int_example.py
num = 10
print("Integer:", num)
print("Type:", type(num))


# float_example.py
pi = 3.14
print("Float:", pi)
print("Type:", type(pi))


# complex_example.py
z = 2 + 3j
print("Complex number:", z)
print("Real part:", z.real)
print("Imaginary part:", z.imag)



# string_example.py
name = "Python"
print("String:", name)
print("Length of string:", len(name))


# list_example.py
fruits = ["apple", "banana", "cherry"]
print("List:", fruits)
fruits.append("orange")
print("Updated List:", fruits)



# tuple_example.py
dimensions = (10, 20, 30)
print("Tuple:", dimensions)
print("Second element:", dimensions[1])




# range_example.py
nums = range(5)
print("Range elements:")
for num in nums:
    print(num)




# dict_example.py
person = {"name": "Alice", "age": 25}
print("Dictionary:", person)
print("Name:", person["name"])



# set_example.py
colors = {"red", "green", "blue", "green"}  # 'green' won't repeat
print("Set:", colors)




# bool_example.py
is_valid = True
print("Boolean:", is_valid)
print("Type:", type(is_valid))
