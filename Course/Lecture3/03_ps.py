import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1.Input
# a = input("Enter Email : ")
# x = a.endswith("@gmail.com")
# b = "Your Welcome" if x else "incorrect Email"
# print(b)

# 2.Template
# from datetime import date 

# b = date.today()
# a = "Sai"
# print("Hello " + a + "\nYou are selected\nDate :",b)

# 3.Finding "  "
# a = "LFG"
# b = a.find("  ")
# x = False if b == -1 else True
# print("Is given string is having a double sapce ?",x)

# 4.Replacing "  "
a = "  LFG"
print(a + "\n" + a.replace("  "," "))