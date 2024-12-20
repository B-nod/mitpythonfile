import os, shutil
# file handling -> open file, close file, read file, write and maintain file
path = 'test.txt'
# my_file = open(path)
# print(my_file)
# print(my_file.read()) #to read the file.
# print(my_file.writable()) # to check whether to write in file or not
# my_file.close()

# my_another_file = open(path, 'r+') # to define the mode and r+ mode means we can read and write the 
# print(my_another_file)
# print(my_another_file.readable()) # to check whether the file can be read or not
# print(my_another_file.writable()) # to check whether the file can be write or not
# print(my_another_file.read()) # to read the file
# my_another_file.write('\n Ram \n') # to write on the file
# my_another_file.close()

# my_another_file = open(path, 'w+')
# print(my_another_file)
# print(my_another_file.read())
# print(my_another_file.readable())
# print(my_another_file.writable())
# my_another_file.write('Ram \n Arjesh')
# print(my_another_file.seek(1))
# print(my_another_file.read())
# print(my_another_file.seek(0))

# my_another_file.close()

# my_next_file = open('next.txt', 'a+')
# print(my_next_file)
# print(my_next_file.writable())
# print(my_next_file.readable())
# my_next_file.write('Hello \n World')
# my_next_file.seek(10)
# print(my_next_file.read())





# print(my_next_file.seek(0))
# print(my_next_file.read())
# list1 = ['\nRam\n','\nShyam\n', '\nhari\n']

# print(my_next_file.seek(0))


# shutil.copy('next.txt', 'next1.txt')

# os.remove('next1.txt')


shutil.move('test.txt', 'next1.txt')
