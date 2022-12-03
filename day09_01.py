file = open('day09_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    source.append(int(temp))

# print(source)

for i in range(25, len(source)):
    ofspring = source[i]
    count_list = []
    for x in range(i-25, i):
        for y in range(x+1, i):
            count_list.append(source[x] + source[y])
    print(count_list)
    if source[i] not in count_list:
        print("Number", source[i], "positon in list (real not Python)", i+1, "is not addiction of foregoing numbers")
        exit()