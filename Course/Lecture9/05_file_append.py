import os
os.system('cls')


str = input("Enter text to append : ")
with open("05_file_append.txt" ,'a') as file :
    file.write(str+"\n")
print("Appending Successed")
