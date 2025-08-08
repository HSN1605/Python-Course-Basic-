import os
os.system('cls' if os.name == 'nt' else 'clear')

s = "Harsainath"
s2 = "hello world"
s3 = "one day he finally understand the assignment"
s4 = "   Welcome to my world   "
print(len(s))


print(s3.upper())
print(s3.lower())
print(s3.title())
print(s3.swapcase())
print(s3.capitalize())

print(s.endswith("ath"))
print(s.startswith("Har"))
print(s3.count("s"))
print(s2.find("world"))
print(s2.index("hell")) # returns error if not found 
print(s2.find("hari")) # returns -1 if not found 

print(s2.replace("hello5","world"))
print(s4.strip())
print(s4.rstrip()) # Removes traling whitespaces 
print(s4.lstrip()) # Removes leading whitespaces 

# Testing Functions
a = "089"
b = "password"
c = "password1;"
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(a.isupper())
print(a.islower())   
print(a.istitle())

# Escape Sequences

print("Create NewLine\n")
print("\tThis is Tab!")
print("\'how is it possible?\'")
print("backslash \\")