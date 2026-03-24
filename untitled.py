Module1_Numbers_and_Types
.1 - Python uses different data types like integers, floats, strings, and booleans. These types help store and manage different kinds of data.
x = 10        # integer
y = 3.14      # float
name = "Nick" # string
is_student = True # boolean
print(type(x))
print(type(y))
print(type(name))
print(type(is_student))

.2 - Integers are whole numbers, while floats contain decimal values. Python will automatically determine the type.
a = 5
b = 5.0
print(type(a))
print(type(b))

.3 - Strings are used to store text and are enclosed in quotes.\
first = "Hello"
last = "World"
print(first + " " + last)

.4 - Type conversion allows changing one data type to another.
num = "10"
converted = int(num)
print(converted)
print(type(converted))

.5 - Mathematical operations can be performed using operators like +, -, *, and /.
x = 10
y = 3

print(x + y)
print(x - y)
print(x * y)
print(x / y)

.6 - Variables store values and can be reused throughout the program.
age = 18
age = age + 1
print(age)