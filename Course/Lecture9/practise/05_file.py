import os
os.system('cls')

cw = ['crazy', 'shit', 'idiot', 'mess']
lines = []
new_lines = []
with open("05_file.txt", 'r') as file :
    lines = file.readlines()
print(lines)

for i in lines :
    for j in cw :
        if i.find(j) != -1 :
            s = i.replace(j,"#"*len(j))
            new_lines.append(s)
            break
        else :
            continue
        
with open("05_file.txt", 'w') as file :
     file.writelines(new_lines)
          