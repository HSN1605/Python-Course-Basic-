import os
os.system('cls' if os.name == 'nt' else 'clear')

# a = (1)
# b = (1,"sb",7.7) # Difference between List  -- Mutable, Tuple -- Immutable
# print(type(a),type(b))
# print(b[0]) # if b[0] = 'j' it throw error because tuple is Immutable

# Methods

tpl = (1,2,7,3,2,1,7,"seven")
print(tpl[0:4]) 

print(tpl.index(7)) # takes value return index if found else error
print(tpl.index(7,1))

print(tpl.count(7))

tpl2 = (2,3)
tpl3 = (4,5)
print(tpl2+tpl3)

print(2 in tpl2)

print(tpl3 * 3)

my_tuple = (1,10,100,1000)
print(min(my_tuple))
print(max(my_tuple))