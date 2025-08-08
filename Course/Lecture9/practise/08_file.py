with open("08_file.txt",'r') as file :
    data = file.read()
with open("08_this.txt",'w') as file :
    file.write(data)
print("Done!!!")