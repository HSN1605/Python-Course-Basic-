import os
os.system('cls')

name = "is"
n = 1
with open("06_file.txt",'r') as file :
    data = file.readlines()
for datalines in data :
    if (f"{name}" in datalines) :
        print(f"{name} present in file,Line no : {n}") 
        break
    n += 1
else :
    print(f"{name} not present in file") 