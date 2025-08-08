# import pyttsx3 
# import pyjokes

# joke = pyjokes.get_joke()
# asst = pyttsx3.init()
# print(joke+'\n')
# asst.say(joke)
# asst.runAndWait()

import os

dict_path = '/Code/Python/Lecture1'
contents = os.listdir(dict_path)

for i in contents:
    print(i)