#function is a block of code. we used function to reuse the code. Two type of function 
# 1. Build-in function
# 2. User defined function

#syntax of function
# def function_name():
#     function body

# function_name()

#simple program in user defined function
def helloworld():
   print("Hello, world!")

helloworld()

# #positional arguments - takes value according to proper positional order.
# def hello(name, course_name): #parameter
#     print("Hello", name, "Welcome to Python Training")
#     print(course_name)

# hello('Python with django', 'Ram') #arguments

# # # #keywords arguments - takes value according to keyword
# def hello(name, course_name): #parameter
#     print("Hello", name, "Welcome to Web development Training")
#     print(course_name)
#     print("I live in")
#     print("I am studying at ")

# hello(course_name='Python with django', name='Ram') #arguments

# #default arguments
def hello(name, course_name='Python with django'): #parameter
    print("Hello", name, "Welcome to Web development Training")
    print(course_name)

hello(name='Ram', course_name='python with data science') #arguments

# #arbitrary arguments - *args

def sum(*args):
    total = 0
    print(args[0]+args[1]+args[2])
    for n in args:
        total+=n
    # total=0+2=2
    # total=2+3=5
    return total  #return gives result of function and stop the excution of function

resutlt = sum(2,3,5,4,5,6)
print(resutlt)


# #arbitrary keyword arguments - **kwargs which contain data in key:value pairs
def hello(**kwargs): #parameter
    print("Hello", kwargs['name'], "Welcome to Web development Training")
    print(kwargs['course_name'])

hello(name='Ram', course_name='Python with Data Science', another_course='Python with Data Science')

# # scope of variable
# # global variable -> which can accessible from any place.
# l = float(input('Enter a length : '))
# w = float(input('Enter a widht : '))

# def area():
#     #local variable -> that is defined inside the function and cannnot accessible from outside the function. its scope is only around the declared function.
#     h = float(input("Enter a height : "))
#     global area_of_object
#     area_of_object = l*w
#     # volume = area_of_object * h
#     return area_of_object

# def volume():
#     h = float(input('Enter a height : '))
#     v = area_of_object* h
#     return v


# result = area()
# result_volume = volume()
# print(result)
# print(result_volume)


# def add():
#     global a, b

#     a = int(input("Enter a first number : "))
#     b = int(input("Enter a second number : "))

#     return a+b

# # def susb():
# # def mult():
# # def pow():
# print(add())

# #lambda function: the function without name. it is used for instant use and its one-time uses. lambda keyword is used.

# x = lambda a,b: a%2==0
# even = x(int(input("Enter an even number : ")))
# print(even)

# def addition(a,b):
#     return a+b

# add = addition(10,15)
# print(add)
# y = lambda a,b: a+b
# addition = y(10,15)
# print(addition)


#addition 
#substraction

# recursive function - fucntion calling itself again and again
# def factorial(n):
#     if n == 0:
#         return 1
#     else:
#         return n*factorial(n-1)

# result = factorial(3)
# print(result)
# #filter()
# #map()

