text = "hello\nminh la thuy"

with open('text.txt','w',encoding= "utf-8") as file: # 'w' -> clear and write text
    file.write(text)

with open('a.txt','a') as file1:   # 'a' -> write in a last file and not clear 
    file1.write(text)