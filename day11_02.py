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
    for i in range(1, wide+1):
        for j in range(1, high+1):
            if matrix[j,i] == 0:
                continue
            
            polar = 0

            # direction right
            ii = 1
            jj = 1
            while True: 
                if i+ii <= wide:
                    if matrix[j, i+ii] == 10:
                        polar += 10
                        break
                    elif matrix[j, i+ii] == 1:
                        break
                else:
                    break
                ii += 1

            # direction down right
            ii = 1
            jj = 1
            while True:
                if i+ii <= wide and j+jj <= high:
                    if matrix[j+jj, i+ii] == 10:
                        polar += 10
                        break
                    elif matrix[j+jj, i+ii] == 1:
                        break
                else:
                    break
                ii += 1
                jj += 1

            # direction down
            ii = 1
            jj = 1
            while True:
                if j+jj <= high:
                    if matrix[j+jj, i] == 10:
                        polar += 10
                        break
                    elif matrix[j+jj, i] == 1:
                        break
                else:
                    break
                ii += 1
                jj += 1

            # direction down left
            ii = 1
            jj = 1
            while True:
                if i-ii >= 1 and j+jj <= high:
                    if matrix[j+jj, i-ii] == 10:
                        polar += 10
                        break
                    elif matrix[j+jj, i-ii] == 1:
                        break
                else:
                    break
                ii += 1
                jj += 1

            # direction left
            ii = 1
            jj = 1
            while True:
                if i-ii >= 1:
                    if matrix[j, i-ii] == 10:
                        polar += 10
                        break
                    elif matrix[j, i-ii] == 1:
                        break
                else:
                    break
                ii += 1
                jj += 1

            # direction up left
            ii = 1
            jj = 1
            while True:
                if i-ii >= 1 and j-jj >= 1:
                    if matrix[j-jj, i-ii] == 10:
                        polar += 10
                        break
                    elif matrix[j-jj, i-ii] == 1:
                        break
                else:
                    break
                ii += 1
                jj += 1

            # direction up
            ii = 1
            jj = 1
            while True:
                if j-jj >= 1:
                    if matrix[j-jj, i] == 10:
                        polar += 10
                        break
                    if matrix[j-jj, i] == 1:
                        break
                else:
                    break
                ii += 1
                jj += 1

            # direction up right
            ii = 1
            jj = 1
            while True:
                if i+ii <= wide and j-jj >= 1:
                    if matrix[j-jj, i+ii] == 10:
                        polar += 10
                        break
                    elif matrix[j-jj, i+ii] == 1:
                        break
                else:
                    break
                ii += 1
                jj += 1

            # print(j,i,polar)
            # input("Waiting ...")

            if matrix[j, i] == 1 and polar < 10:
                tempix[j, i] = 10
                lock = 1
            elif matrix[j, i] == 10 and polar >= 50:
                tempix[j, i] = 1
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