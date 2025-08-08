import os
os.system('cls' if os.name == 'nt' else 'clear')

# li = ["apple", "banana", 7, 10.2]
# print(li[0])
# li[0] = "Dragon Fruit"
# print(li[0]) # means lists are imutable anlike strings
# print(li[0:2])
# print(li)

# Meathods 

lst = ['a', 'b', 'c']

lst.append('e')
print(lst)

lst2 = ['f']
lst.extend(lst2)
print(lst)

lst.insert(3,'d')
print(lst)

lst.remove('f')
print(lst)

print(lst.pop(4))

lst.reverse()
print(lst)

lst.sort()
print(lst)

print(lst.count('a'))

lst.clear()
print(lst)