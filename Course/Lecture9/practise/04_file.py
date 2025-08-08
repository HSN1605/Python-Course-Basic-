import os
os.system('cls')

content = ''
with open('04_file.txt', 'r') as file :
    content = file.read()
content = content.replace("monkey","*****")
with open('04_file.txt', 'w') as file :
    file.write(content)