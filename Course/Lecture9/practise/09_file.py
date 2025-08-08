with open("09_file.txt",'r') as file :
    data = file.read()
with open("09_file2.txt",'r') as file :
    data2 = file.read()
if (data.lower()).strip() == (data2.lower()).strip() :
    print("Content Matched")
else :
    print("No content match")