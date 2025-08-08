import os
os.system('cls' if os.name == 'nt' else 'clear')

product = {
    1 : "apple",
    2 : "grape",
    "3" : "orange"
}

print(product)

dict = {} #empty dictionary
print(type(dict))

# Methods

print(product.keys())

print(product.values())

print(product.items())

print(product.get(5)) # if key exist give value else None
print(product[1])     # if key exist give value else Error 

product.update({"4" : "banana"})
print(product)

my_dict = {
    "apple" : 100,
    "banana": 20,
    "grapes": 40
}

value = my_dict.pop("apple")
print(value)
print(my_dict)


item = product.popitem()
print(item)
print(product)
