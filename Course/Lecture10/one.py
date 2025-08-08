with open("new.txt", 'r') as file :
    data = file.read()
    print(data)
with open("write.txt", 'w') as file2 :
    file2.write(data)
