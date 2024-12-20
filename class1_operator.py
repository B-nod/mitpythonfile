# operator is a symbol which is used to perform certain operation.
# 1. Arthemetic operator, %
# symbol
# +, - , *, /, %(remainder), //(floor division), **(power) 

# x = 1
# y = 1
# a = '1'
# b = '1'
# print(x+y)
# print(x-y)
# print(x*y)
# print(x/y)
# print(x%y)
# print(x**y)
# print(x//y)
# print(a+b)
# num = int(input("Enter a number : "))
# num_2 = int(input("Enter an another number : "))
# print(num+num_2)
# 2. Assignment operator
# x+=y => x=x+y
# x-=y => x=x-y
# x*=y => x=x*y
# x/=y => x=x/y
# x%=y => x=x%y
# x**=y => x=x**y
# x//=y => x=x//y
a = 2
b = 4
a**=b
print(a)

# 3. Comparision operator 
# == equal to
# > greater than
# < lower than
# >= greater than and equal to
# <= lower than and equal to
# != not equal to

data = 5
print(data>4)

# 4. Logical operator
# and gives true when all equation are true
#True and True = True
# True and False = False
# False and True = False
# False and False = False
print(data==4 and data ==5)

# or gives false when all arguments are false
# True or True = True
# True or False = True
# False or True = True
# False or False = False
print(data==4 or data ==5)

# # not it make the true statement into false and vice versa.
print(not(data==4 or data ==5))

# # 5. Membership 
# # in , not in
num_list = [1,2,3,4,5,6,7,8,9]
x = 10
print(x in num_list)
print(x not in num_list)

# # 6. Indentity operator
# # is , is not
x = 10
print(id(x))
y = 10
print(id(y))
listx = [1,2,3]
print(id(listx))
listy=[1,2,3]
print(id(listy))
print("This is an identity opertor output : ", x is y)
print("This is an identity opertor output : ", listx is not listy)


# # 7. Bitwise operator