import random
import os
os.system('cls' if os.name == 'nt' else 'clear')

def get_choice(n):
    my_dict = {
         1 : 'r',
         2 : 'p',
         3 : 's'
    }
    return my_dict.get(n)


yp,cp = 0,0
r,p,s = 'r','p','s'

for i in range(3) :
    print("------------------ Round",  i+1 ," -----------------------")
    n = random.randint(1,3)
    print("Optons are :\n1.Rock\n2.Paper\n3.Scissor")
    m = int(input("Enter Your Choice number : "))
    you = get_choice(m)
    computer = get_choice(n)
    if you == r and computer == p :
        print("Your : " + you + " and Computer : " + computer , end = ' ')
        print("You Lost Round ",i+1)
        cp += 1
    elif you == p and computer == s :
        print("Your : " + you + " and Computer : " + computer, end = ' ')
        print("You Lost Round", i+1)
        cp += 1
    elif you == s and computer == r :
        print("Your : " + you + " and Computer : " + computer, end = ' ')
        print("You Lost Round", i+1)
        cp += 1
    elif computer == r and you == p :
        print("Your : " + you + " and Computer : " + computer, end = ' ')
        print("You Won Round", i+1)
        yp += 1
    elif computer == p and you == s :
        print("Your : " + you + " and Computer : " + computer, end = ' ')
        print("You Won Round", i+1)
        yp += 1
    elif computer == s and you == r :
        print("Your : " + you + " and Computer : " + computer, end = ' ')
        print("You Won Round", i+1)
        yp += 1
    else :
        print("Your : " + you + " and Computer : " + computer, end = ' ')
        print(f"Round {i+1} Draw")
if yp > cp :
    print("You Won the Match!!!")
else :
    print("Computer Won the Match!!!")
