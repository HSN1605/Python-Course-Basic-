import os
os.system('cls' if os.name == 'nt' else 'clear')

my_file = open("01_file_read.txt", "r")
content = my_file.read()
print(content)
my_file.close()