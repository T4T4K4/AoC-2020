file = open('day01_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
source = []

for line in lines:
    source.append(int(line[:-1]))

source = [1721,979,366,299,675,1456]

result = []

for i,nmb1 in enumerate(source):
    for j in range(i + 1, len(source)):
        if (i != j) and ((nmb1 + source[j]) == 2020):
             result.append([ i+1, nmb1, j+1, source[j]])

print(result)
x = result[0][1] * result[0][3]
print(x)

