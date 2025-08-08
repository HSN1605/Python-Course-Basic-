import os
import random
os.system('cls')
def game():
        n = random.randint(1,100)
        with open("02_file.txt",'a') as file :
            if n > 70 :
                txt = "Hiscore -- " + str(n) + '\n'
                file.write(txt)
            else :
                print(n)
                print("End")
for i in range(10):
    game()