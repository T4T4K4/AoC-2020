file = open('day14_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    temp1 = temp.split(" = ")
    if temp1[0] != "mask":
        temp1 = [int(temp1[0][4:-1]), int(temp1[1])]
    source.append(temp1)

print(source)

memories = {}

for line in source:
    if line[0] == "mask":
        mask = line[1]
    else:
        value = format(line[1], '#038b')
        value = value[2:]
        
        # print(value, int(value, 2))
        # print(mask)
        for i in range(len(value)):
            if mask[i] != "X":
                value = value[:i] + mask[i] + value[i+1:]
        memories[line[0]] = int(value, 2)
        print(value, int(value, 2))
    # print("***********************")

# print(memories)

summary = sum(memories.values())
print(summary)
print(bin(summary))