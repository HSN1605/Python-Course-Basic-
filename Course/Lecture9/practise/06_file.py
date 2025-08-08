import os
os.system('cls')

name = "lorem"
n = 1
with open("06_file.txt",'r') as file :
    data = file.readl()
if (f"{name}" in data) :
    print(f"{name} present in file") 

else :
    print(f"{name} not present in file") 
