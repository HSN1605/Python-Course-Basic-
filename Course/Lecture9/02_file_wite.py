import os
os.system('cls')

content = "Good Morning Nellore"
my_file = open("02_file_wite.txt", "w")
my_file.write(content)
print("content loaded successfully!")
my_file.close()