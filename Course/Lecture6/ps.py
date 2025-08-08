import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1. max of 4

# a,b,c,d = map(float, input("Enter a,b,c and d : ").split())
# m = max(a,b,c,d)
# print(m)

# 2. marks

# list = []
# sf = 0
# sum = 0
# for i in range(0,3) : 
#     a = float(input("Enter marks: "))
#     if a < 33 : 
#         sf += 1
#     sum += a    
#     list.append(a)
# per = float((sum/300)*100)
# if sf == 0 and per >= 40 :
#     print("You got = ",per,"%\nYou are Passed")
# else:
#     print("You got = ",per,"%\nSubjects Failed = ",sf,"\nYour Failed,Better luck next time")

# 3.Spam detection

# txt = input("Enter the message you recevied : ")
# if txt == "click here" or txt == "subscribe now" or txt == "click button" or txt == "make a lot of money" or txt == "buy now" :
#     print("Spam Detected!!!")
# else :
#     print("Ensure this is legit, as we didn't found any flaws")    

# 4.Username
# name = input("enter user id : ")
# n = len(name) 
# if (n < 3 or n > 10) :
#     print("An userId must be greater an 3, less than 10 charaters")
# else :
#     print("Valid Userid")

# 5.Selected List 

# selected_list = ["Hari", "Sai", "Nath", "Sriman", "Bhuvana", "Sumathi"]
# name = input("Can i know your Name sir/madam : ")
# if name.capitalize() in selected_list :
#     print("Your name is in the list")
# else :
#     print("Your name is not there in list")

# 6.Grade

# m = float(input("Enter your marks : "))
# lm = False if m > 100 or m < 0 else True
# g = []
# if lm == False :
#     print("You have entered invalid marks.")
#     exit()
# else:
#     if m > 90 : 
#         g.append('Ex')
#     elif m > 80 and m < 90: 
#         g.append('A')
#     elif m > 70 and m < 80: 
#         g.append('B')
#     elif m > 60 and m < 70: 
#         g.append('C')
#     elif m > 40 and m < 60: 
#         g.append('D')
#     else:
#         g.append('F')
#     print("Your Grade is ",g)

# 7. finding

# word = input("Enter which word you want to find in post : ").lower()
# post = "Today an accident is happend at nellore"
# mp = post.lower()
# con = True if mp.find(word) != -1 else False
# if con :
#     print("Post is talking about " + word.capitalize())
# else :
#     print("Post is not talking about " + word.capitalize())

# --or

word = input("Enter which word you want to find in post : ").lower()
post = "Today an accident is happend at nellore".lower()
if word in post :
    print("Post is talking about " + word.capitalize())
else :
    print("Post is not talking about " + word.capitalize())


