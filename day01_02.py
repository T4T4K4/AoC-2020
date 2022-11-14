file = open('day01_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
source = []

for line in lines:
    source.append(int(line[:-1]))

# source = [1721,979,366,299,675,1456]

result = []

for i,nmb1 in enumerate(source):
    for j,nmb2 in enumerate(source):
        for k,nmb3 in enumerate(source):
            if not( i == j or j == k or i == k ):
                if ( nmb1 + nmb2 + nmb3 ) == 2020:
                    result.append([ i+1, nmb1, j+1, nmb2, k+1, nmb3])

print(result)
x = result[0][1] * result[0][3] * result[0][5]
print(x)

# 979 366 675