# 1. Print Sentences
# quotes = "There are no shortcuts to any place worth going.\nI think it's possible for ordinary people to choose to be extraordinary.\nI find that the harder I work, the more luck I seem to have.\nGenius is 10%/ inspiration, 90%/ perspiration.\n"
# print(quotes)

# 3. Use Modules

# from PyDictionary import PyDictionary
# dictionary = PyDictionary()
# print(dictionary.meaning("important"))

# import pyqrcode
# import png

# q = pyqrcode.create(input("Enter prompt: "))
# q.png('qr.png',scale=10)
# print("Qr Generated")

# 4. OS module

import os

# Example dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'Wonderland'
}

# Optional: Clear the console for a cleaner output (works on Windows and Unix)
os.system('cls' if os.name == 'nt' else 'clear')

print(os.name)

for key, value in my_dict.items():
    print(f"{key}: {value}")
