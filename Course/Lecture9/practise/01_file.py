import os
os.system('cls')

find = False
word = 'whisper'
with open("01_file.txt") as file:
    li = file.readlines()
    for i in li :
        if (i.lower()).find(word.lower()) == -1 :
            find = False
        else :
            find = True
            break

if find == True : 
    print(word + " exist in file.txt !!")
else :
    print(word + " is not there")
