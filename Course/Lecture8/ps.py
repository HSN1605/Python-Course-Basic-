import os
os.system('cls' if os.name == 'nt' else 'clear')

# 1.max of three

# def highest(li) :
#     return max(li)

# print(highest([1,2,3,8,77]))

# 2.Cel - Fah

# c = 10
# f = (1.8 * c ) + 32
# print("F = ",f )

# 3.Prevent new line

# print('Hello',end='')
# print('World',end='')

# 4.Sum of n

# def adder(n) :
#     sum = 0
#     if n == 0 :
#         return sum
#     else :
#         sum = n + adder(n-1)
#     return sum
# a = adder(7)
# print(a)

# 5. pattern 

# def inverted_triange(n):
#     for i in range(n):
#         print('*' * (n-i))
#     print()
# inverted_triange(3)

# 6.inch to cms

# i = 5
# cm = i * 2.54 # 1 inch  == 2.54 centimeter
# print(cm)

# 7.Tables

# def tableof(n,i = 1) :
#     if i>10 :
#         print("Finished")
#     else :
#         print(n ,"*",i,"=",n*i)
#         tableof(n,i+1)
# tableof(7)

# 8. list

# def list_manager(list,word) :
#     list.remove(word)
#     return list
# li = [1,2,33,4]
# print(list_manager(li,33))