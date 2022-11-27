import numpy
import math

file = open('day16_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

mask = []
tickets_old = []
tickets = []
for line in lines:
    if ": " in line:
        temp1 = line.strip("\n")
        type = temp1.split(": ")[0]
        temp2 = temp1.split(": ")[1]
        temp3 = temp2.split(" or ")
        temp_a = temp3[0].split("-")
        temp_b = temp3[1].split("-")
        mask.append([type, [int(temp_a[0]), int(temp_a[1])], [int(temp_b[0]), int(temp_b[1])]])
    elif line == "\n" or "your" in line or "nearby" in line:
        continue
    else:
        temp1 = line.strip("\n")
        temp2 = temp1.split(",")
        tickets_old.append([int(i) for i in temp2])

old_result = []
tickets.append(tickets_old[0]) # append my ticket

for set in tickets_old[1:]:
    lock = 0
    for number in set:
        for range_ in mask:
            cond_a = range_[1][0] <= number <= range_[1][1]
            cond_b = range_[2][0] <= number <= range_[2][1]
            if cond_a or cond_b:
                lock += 1
                print(number)
                break

    if lock == 20:
        tickets.append(set)

ar = len(tickets[0])
matrix = numpy.zeros((ar, ar), dtype='int8')

for k, field in enumerate(mask):
    for i in range(len(tickets[0])):
        lock = 0
        for j in range(len(tickets)):
            cond_a = field[1][0] <= tickets[j][i] <= field[1][1]
            cond_b = field[2][0] <= tickets[j][i] <= field[2][1]
            if not (cond_a or cond_b):
                lock = 1
                break
        if lock == 0:
            matrix[k,i] = 1

result = []
# rows are mask
# columns are ticket fields (collumns)
# print(matrix)

for cc in range(len(mask)):
    select = numpy.sum(matrix, axis=1)
    for i, s in enumerate(select):
        if s == 1:
            x, = numpy.where(matrix[i] == 1)
            # i is type of field, x[0] is position of ticket field
            result.append([i, x[0]])
            matrix[:,x[0]] = 0

# print(result)

values = []

for i in result:
    value = tickets[0][i[1]]
    if mask[i[0]][0][:5] == "depar":
        values.append(value)
    print("Type", mask[i[0]][0], "is", i[1], "field in ticket and it is", value, "value")

print(values)
print(math.prod(values))

result = 1
for x in values:
    result = result * x

print(result)
