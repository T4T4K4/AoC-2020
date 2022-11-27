file = open('day16_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

mask = []
tickets = []
for line in lines:
    if ": " in line:
        temp1 = line.strip("\n")
        temp11 = temp1.split(": ")[1]
        temp2 = temp11.split(" ")
        temp_a = temp2[0].split("-")
        temp_b = temp2[2].split("-")
        mask.append([int(temp_a[0]), int(temp_a[1])])
        mask.append([int(temp_b[0]), int(temp_b[1])])
    elif line == "\n" or "your" in line or "nearby" in line:
        continue
    else:
        temp1 = line.strip("\n")
        temp2 = temp1.split(",")
        tickets.append([int(i) for i in temp2])

old_result = []

for set in tickets[1:]:
    for number in set:
        lock = 0
        for range_ in mask:
            # print(range_[0], number, range_[1])
            if range_[0] <= number <= range_[1]:
                
                # input("enter")
                lock = 1
        
        if lock == 0:
            old_result.append(number)

print(old_result)
print(sum(old_result))