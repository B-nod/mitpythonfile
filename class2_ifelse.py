x = int(input("Enter your number: "))

#if else statement
if x >=18:
   print("Given number is positive numebr")
else:
    print("Given number is negative number")

#elif statement
if x >0:
    print("Given number is positive number")
elif x ==0:
    print("Given number is equal to zero")
else:
    print("Given number is negative")

# nested if else statement
if x>=0:
    if x ==0:
        print("Given is equal to zero")
    else:
        print("Given number is positive")
else:
    print("Given number is negative")