import os
os.system('cls' if os.name == 'nt' else 'clear')

# s = {1,1, "one"}
# es = set()
# print(s)
# print(es)
# print(type(s))
# print(type(es))

# Methods

x = {1,2,3}

# x.add(4)
# print(x)

# x.update([4,5])
# print(x)

# x.remove(4)
# print(x)

# x.discard(5)
# print(x)


# print(x.pop())

# x.clear()
# print(x)

a = {1,2,3}
b = {3,4,5}

print("a | b : ",a.union(b))

print("a & b : ",a.intersection(b))

print("a - b : ",a.difference(b))

print("b - a : ",b.difference(a))

print("b ^ a : ",b.symmetric_difference(a))

p = {1,4}
print("Is p subset of a ?",p.issubset(a))
print("Is a superset of p ?",a.issuperset(p))