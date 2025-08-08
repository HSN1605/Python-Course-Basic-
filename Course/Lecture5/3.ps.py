import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1. dictionary 

# dict = {
#     "namaste" : "hello",
#     "vidya" : "education",
#     "pustakam" : "book",
#     "mandulu"  : "medicine",
#     "vidhyam" : "treatment",
#     "kashtam" : "difficult",
#     "sulabam" : "easy"
# }
# a = input("Welcome to Telugu to English Traslation Service\nEnter Telugu word : ")
# print(a, " : ",dict.get(a))

# 2.Set 1

# s = set()
# for i in range(0,8):
#     a = input("Enter value : ")
#     s.add(a)
# print(s)

# 3.Set 2

# s = {7,"7"}
# print(s,type(s))

# 4. set 4

# s = {7}
# s.add(7.0)
# s.add("7")
# print(s,len(s))

# 5. Dict - Empty
# d = {}
# print(type(d)) # empty dict 

# 6. Dict 1

# d = {}
# for i in range(0,4):
#     a = input("Enter your Name : ")
#     b = input("Enter your Favourite Language : ")
#     d.update({a:b})
# print(d)

# 7. set 


# s = {1,2,3,"4",[5,6]} # Since set is hashable and list is unhashable it is Invalid, 
st= {1,2,3,"4",(5,6)} # Since set is hashable and tuple is hashable it is Valid, 
print(len(st))