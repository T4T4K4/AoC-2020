import numpy

file = open('day11_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    source.append(temp)

wide = len(source[0])
high = len(source)

print(wide,high)

matrix = numpy.zeros((high + 2, wide + 2), dtype='int8')


for i in range(wide):
    for j in range(high):
        if source[j][i] == "L":
            matrix[j+1,i+1] = 1

'''
print(source[0])
print(len(source[0]), len(source))
print(matrix[1])
print(len(matrix[1]), len(matrix))
'''

tempix = numpy.copy(matrix)

while True:
    lock = 0
    for i in range(wide):
        for j in range(high):
            if matrix[j+1, i+1] == 1 and numpy.sum(matrix[j:j+3, i:i+3]) < 10:
                tempix[j+1, i+1] = 10
                lock = 1
            elif matrix[j+1, i+1] == 10 and numpy.sum(matrix[j:j+3, i:i+3]) >= 50:
                tempix[j+1, i+1] = 1
                lock = 1
    matrix = numpy.copy(tempix)
    if lock == 0:
        break

occu_seat = 0
for i in range(wide):
    for j in range(high):
        if matrix[j+1, i+1] == 10:
            occu_seat += 1

print(matrix)
print("Occupied seats are:", occu_seat)