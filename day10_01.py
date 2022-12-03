file = open('day10_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    source.append(int(temp))

source.sort()
source.insert(0, 0)
source.append(max(source) + 3)
final_jolt = 22
diff_list = []

print(source)

for i in range(1, len(source)):
    
    diff = source[i] - source[i-1]
    diff_list.append(diff)

    # print(source[i], diff)

    '''
    if final_jolt - source[i] < 3:
        print("Error, no result for this set of adapteurs")
        exit()
    elif final_jolt - source[i] == 3:
        break
    '''

print(diff_list)

count_1 = diff_list.count(1)
count_3 = diff_list.count(3)

print("Diference 1 count is:", count_1)
print("Diference 3 count is:", count_3)
print("Result is:", count_1 * count_3)