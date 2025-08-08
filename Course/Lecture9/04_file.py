import os
os.system('cls' if os.name == 'nt' else 'clear')

list = ['Hi iam 1\n','Hi iam 2\n','Hi iam 3\n','Hi iam 4\n','Hi iam 5\n','Hi iam 6\n','Hi iam 7\n']

with open("04_file.txt",'w') as my_file :
    my_file.writelines(list)
    print("Check the file")



