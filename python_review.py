# python revisited

# Data Types
# Int 1
# Float 1.1
# String '' or ""
# Bool 
#True  1
#False  0

# output and printing
print("something", 4.5, end="|") # the comma add a space in between
print("something", end='\n')
print("next line")

# variables
hello = "Ralph"
print(hello, "world")

#naming convention: no start with number or special characters, and use _ to seperate variable

# Input
#data = input("prompt: ") everything in the input data will be string
#print(data)

# data manipulation
x = 9
y = 3
result = int(x / y)
print(result)

hello = "hello world".upper()
print(hello, type(hello), hello.count('O'))

# conditional operator
"""
==
>
<
>=
<=

and 
or
not

order of operation: not, and, or
"""

print(not (True and False or False))

# if
x = 1

if x == 1:
    print(x)
elif x == 2:
    print(x)
else:
    print("No")


# list and tuple
x = [1,2,3,4,5]
x.append("x")
x.extend([6,6,6,6,6,7])
x.pop()
print(x[1], x[2])


# for loop while loop
for i in range(10): #range(stop)
    print(i)
# range(start, stop, step)
for i in range(0, 20, 2):
    print(i)

x = [1,2,3,4,5]

for i in [1,2,3,4,5]:
    print(i)

for index, element in enumerate(x):
    print(index, element)

# while condition == something: do something
i = 0
while i < 10:
    i += 1
    x.append("hehe")
    print(x)

# slice operator, sliced = [start:stop:step], works on string, list, and tuple

sliced = x[::-1]
print(sliced)

# set {...}
# but if you want to create an empty set, use x = set(), because x = {} returns a dictionary
x = {1,2,3,4}
print(4 in x) #look faster than a list

# dictionary: {'key': "value"}
x = {'key': 4}
x['key2'] = 5
x[2] = [2,3,4,5]
print(x)
print('key2' in x)
print(x.values())
print(list(x.values()))
print(list(x.keys()))
del x['key']
print(x)
print(x['key2'])
for key, value in x.items():
    print(key, value)

# comprehension, a one line initialization of list, tuple, dict, and others
# var = data type(thing will be added for thing in range(something))
x = [x for x in range(5)]
print(x)

x = [[0 for x in range(2)]for x in range(5)]
print(x)

# function
def func(x, y, z=None):
    print("Run")
    return x * y, x / y

r1,r2 = func(5,6)
print(r1,r2)

# unpackk operator / *args (arguments) and **kwargs (key word arguments, like dictionary)
def func(x):
    def func2():
        print(x)

    return func2

x = func(3)
x()

def func(*args, **kwargs):
    pass

x = [1,2,3,4,5]
print(*x)

# exception
try:
    x = 7 / 0

except Exception as e:
    print(e)
finally:
    print("this runs however")

#lambda a one line anonymous function, just like js's arrow function
x = lambda x: x+5
print(x(2))

# map and filter
x = [12,3,4,5,6,7,5433,4554,32113,4455332,22332,1,2,2,2,2]

mp = map(lambda i: i+2, x)
print(list(mp))

mp = filter(lambda i: i % 2 == 0, x)
print(list(mp))

# f string, just like js `${}`

x = f'hello {6 + 8}'
print(x)