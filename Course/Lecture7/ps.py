import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1.tables 

# n = int(input("Enter n : "))
# print("Multiplication table of ",n)
# for i in range(10):
#     print(n," * ", i+1 ," = ", n*(i+1))

# 2. Greet 

# li = ["hari","sai","nath","sumathi","tarak","koti","suman","shubham"]
# for i in li :
#     if i.startswith("s") :
#         print("Good Morning " + i)
#     else :
#         continue

# 3. whileloop_tables

# n = 1 
# i = 0
# while i < 10 :
#     print(n," * ", i+1 ," = ", n*(i+1))
#     i += 1
    
# 4.prime

# n = 100
# s = set()
# for j in range(2,n) : 
#     for i in range(2,int(j**0.5)+1) :
#         if j % i == 0 :
#             break
#     else : 
#         s.add(j)
# print("Prime Number : ",s)



# 5.Sum of numbers

# n = int(input("Enter the number : "))
# sum = 0
# i = 1
# while i <= n :
#     sum += i
#     i += 1
# print(sum)

# 6.factorial for

# n = int(input("Enter the number : "))
# fac = 1
# if n < 0 :
#     print("Factorial Dooes not exist for negative numbers")
# else :
#     for i in range(1,n+1) :
#         fac *= i
#     print(str(n)+"! = ",fac)

# 7.pattern 1

# n = 5 
# for i in range(1,n+1) : 
#     print("*" * i)

# n = 5 
# for i in range(n+1,0,-1) : 
#     print("*" * i)


# 8. pattern 2

# n = 5
# for i in range(n) :
#     print(' ' * (n-i) + '^' * (2 * i -1)  )

# 9.pattern 3.

# r = 7
# c = 7

# for i in range(r):
#     for j in range(c):
#         if i == 0 or j == 0 or i == r-1 or j == c-1 :
#             print("*",end="")
#         else:
#             print(' ',end='')
#     print()

# 10.tables turned 

# n = 3
# print("Multiplication table of ",n)
# for i in range(10,0,-1):
#     print(n," * ", i ," = ", n*i)