import os
os.system('cls' if os.name == 'nt' else 'clear')

my_file = open("03_file.txt")

# print(my_file.readlines())

# print(my_file.readline())

for lines in my_file:
    print(lines ,end = '')

my_file.close()