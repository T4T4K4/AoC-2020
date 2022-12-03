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
    # print(count_list)
    if source[i] not in count_list:
        print("Number", source[i], "positon in list (real not Python)", i+1, "is not addiction of foregoing numbers")
        result = source[i]
        break

print(result)

for i in range(len(source)):
    temp_result = 0
    temp_list = []
    for j in range(i, len(source)):
        temp_result += source[j]
        if temp_result == result:
            print("Sequence is from", i, "to", j)
            for k in range(i,j+1):
                temp_list.append(source[k])
            print(temp_list)
            print("Max:", max(temp_list))
            print("Min:", min(temp_list))
            print("Result of all is add of max and min:", max(temp_list) + min(temp_list))
            exit()
        elif temp_result > result:
            break