file = open('day10_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    source.append(int(temp))

source.sort()
source.insert(0, 0)
max_ = max(source)
source.append(max_ + 3)
source.append(max_ + 10)
source.append(max_ + 10)

way_counter = []

for mbr in source:
    way_counter.append([mbr, 0])

way_counter[-3][1] = 1
print(source)
print(way_counter)

for i in range(len(way_counter) - 4, -1, -1):
    # diff_1 = diff_2 = diff_3 = 0

    # print(diff_1, way_counter[i+1], way_counter[i])
    
    diff_1 = way_counter[i+1][0] - way_counter[i][0]
    diff_2 = way_counter[i+2][0] - way_counter[i][0]
    diff_3 = way_counter[i+3][0] - way_counter[i][0]

    print(diff_1,diff_2,diff_3)

    temp_counter = way_counter[i+1][1]
    if diff_2 < 4:
        temp_counter += way_counter[i+2][1]
    if diff_3 < 4:
        temp_counter += way_counter[i+3][1]

    way_counter[i][1] = temp_counter

print(way_counter)




