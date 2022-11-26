file = open('day06_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.read()
file.close()

source = []
temp = lines.split("\n\n")
for group in temp:
    temp1 = group.split("\n")
    source.append(temp1)

key = "abcdefghijklmnopqrstuvwxyz"
suma = 0
for group in source:
    char_list = ""
    for mmbr in group:
        
        for char in mmbr:
           if not (char in char_list):
                char_list += char
    suma += len(char_list)

print(suma)