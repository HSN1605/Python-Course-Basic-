import os
os.system('cls' if os.name == 'nt' else 'clear')

# n = str(input("Enter your mobile number : "))
# x = n.startswith("+91")
# if x : 
#     print("Your having an Indian Phone Number")
# else :
#     print("It is not an Indian Phone Number")

# n = int(input("Enter your age : "))
# con = input("Enter your Country International dailing code : ")
# if n >= 18 and con == "+91" :
#     print("Your are Eligible")
# elif n >= 18 and con != "+91" :
#      print("Your are Rejected\nYou have to be an Indian")
# elif n < 18 and con == "+91" :
#      print("Your are Rejected\nYou have to be a Major")
# else : 
#      print("You are Rejected")


print("------------------------------------And gate---------------------------------------")
print("Enter inputs in boolean type")
a = input("Enter a input : ") == "True"
b = input("Enter b input : ") == "True"
print(a,b)

if a and b : 
    print("a & b = ", True)
else :
    print("a & b = ", False)