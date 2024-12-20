# loop is repetation or iteration

# positive_num = [1,2,3,4,5,6]

# for x in positive_num:
#     print(x)

# x = int(input("Enter a number : "))
# for i in range(1,11):
#     # print(x,"X",i, "=",i*x)
#     print(f"{x} x {i} = {i*x}")


# while loop
# y = 1
# while y<=10:
#     print(y)
#     y+=1


#nested loop
# outter loop
for i in range(1,10):
    # inner loop
    for x in range(1,10):
        print(f"{i} X {x} = {i*x}")

for i in range(1,11):
    x = 1
    while x<=10:
         print(f"{i} X {x} = {i*x}")
         x+=1

# while inside while
# while inside for

# break
# continue
# pass

for a in range(1,11):
     if a == 5:
          break
     print(a)

for a in range(1,11):
    if a%2 ==0:
        continue
    print(a)

for a in range(1,11):
    pass
     