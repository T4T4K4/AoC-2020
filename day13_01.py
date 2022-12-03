import math

file = open('day13_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

timestamp = int(lines[0].strip("\n"))

temp = lines[1].strip("\n")
temp1 = temp.split(",")

source = []
for memb in temp1:
    if memb != "x":
        source.append(int(memb))

print(timestamp)
print(source)

bus_ts = []
for bus in source:
    count = math.ceil(timestamp / bus)
    bus_ts.append(count * bus)

print(bus_ts)

result = []
for i in range(len(source)):
    result.append([source[i], bus_ts[i]])

result.sort(key=lambda x: x[1])

print(result)
print("Multiply bus ID by its arrive time:", result[0][0] * (result[0][1] - timestamp))

