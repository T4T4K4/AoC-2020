file = open('day06_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.read()
file.close()

source = []
temp = lines.split("\n\n")
for group in temp:
    temp1 = group.split("\n")
    source.append(temp1)

key = "abcdefghijklmnopqrstuvwxyz"
sumy = []

for group in source:
    deuce = ""
    deuce = group[0]
    for u, unit in enumerate(group[1:]):
        deuce_temp = ""
        for char in unit:
            for d in deuce:
                if char == d:
                    deuce_temp += char
        deuce = deuce_temp
    sumy.append(len(deuce))
            
print(sumy)
print(sum(sumy))