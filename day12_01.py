file = open('day12_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    source.append([temp[:1],int(temp[1:])])

ship = [0,0,0]

for inst in source:
    if inst[0] == "N":
        ship[1] -= inst[1]
    elif inst[0] == "S":
        ship[1] += inst[1]
    elif inst[0] == "E":
        ship[0] += inst[1]
    elif inst[0] == "W":
        ship[0] -= inst[1]
    elif inst[0] == "L":
        ship[2] = (ship[2] - inst[1]) % 360
    elif inst[0] == "R":
        ship[2] = (ship[2] + inst[1]) % 360
    elif inst[0] == "F":
        if ship[2] == 0:
            ship[0] += inst[1]
        elif ship[2] == 180:
            ship[0] -= inst[1]
        elif ship[2] == 90:
            ship[1] += inst[1]
        elif ship[2] == 270:
            ship[1] -= inst[1]
        else:
            print("Angle error")
            exit()
    else:
        print("Instruction error")
        exit()

print(ship)
result = abs(ship[0]) + abs(ship[1])
print("Value of Manhatan distance is:", result)


