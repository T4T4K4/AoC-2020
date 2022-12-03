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

# print(source)

memories = []

for line in source:
    if line[0] == "mask":
        mask = line[1]
    else:
        value = line[1]
        address = format(line[0], '#038b')
        address = address[2:]
        
        # print(line[0])
        # print(mask)

        result = ""
        for i in range(len(address)):
            if mask[i] == "X":
                result += "X"
            elif mask[i] == "1":
                result += "1"
            else:
                result += address[i]

        memories.append([result, line[1]])

# print()
# for xx in memories:
    # print(xx)

memo_dict = {}

for line in memories:
    mem_set = ["b"]
    for bit in line[0]:
        if bit == "0":
            for n in range(len(mem_set)):
                mem_set[n] += "0"
        elif bit == "1":
             for n in range(len(mem_set)):
                mem_set[n] += "1"
        elif bit == "X":
            temp_set = []
            for mem in mem_set:
                temp_set.append(mem + "1")
                temp_set.append(mem + "0")
            mem_set = temp_set.copy()
    
    for i in mem_set:
        mem_pos = int(i[1:], 2)
        # print(i, line[1])
        # print(i[1:], mem_pos)
        memo_dict[mem_pos] = line[1]
        
summary = sum(memo_dict.values())

print(summary)








