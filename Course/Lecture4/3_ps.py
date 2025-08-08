import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1.List

# li = []
# for i in range (0,7) :
#     a = input("Enter item : ")
#     li.append(a)
# print(li)    

# 2.Marks

# li = []
# for i in range (0,6) :
#     a = int(input("Enter marks : "))
#     li.append(a)
# li.sort()    
# li.reverse()    
# print(li)   


# 3.Sum of list

# li = []
# s = 0
# for i in range (0,4) :
#     a = int(input("Enter number : "))
#     li.append(a)
#     s += a
# print("List : " , li)    
# print("Average : ", s/4)  # average

# 4. No.of 0

# tpl = (0,1,2,3,0,4)
# print(tpl.count(0))
# print(tpl.index(0,2))

# 5.Tuple cannot be changed

tpl = (1,2,4)
print(tpl)
tpl[2] = 3 # throw error because tuple is immutable we cannot change it using assignment operator
print(tpl)
