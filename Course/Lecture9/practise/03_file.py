import os
os.system('cls')
with open('03_file.txt','w') as file :
    for i in range(2,21) :
        file.write("Multiplication Table : "+str(i)+'\n')
        for j in range(1,11) :
            file.write(str(i)+'*'+str(j)+'='+str(i*j)+'\n')
print("Finished")