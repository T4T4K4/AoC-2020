import numpy

file = open('day04_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.read()
file.close()

# print(lines)
# print()

source = lines.split("\n\n")
fields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid", "cid"]

pas_valid = []

for i,passport in enumerate(source):
    validation = 0
    pas_valid.append([])
    for f in fields:
        if f in passport:
            pas_valid[i].append(1)
        else:
            pas_valid[i].append(0)
    validation = numpy.sum(pas_valid[i][:-1])
    # print(validation)
    if validation >= 7:
        pas_valid[i].append(1)
    else:
        pas_valid[i].append(0)
    

count_v = 0
for v in pas_valid:
    # print(v)
    count_v += v[8]

print(count_v)


