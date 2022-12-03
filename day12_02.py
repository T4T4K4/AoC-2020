file = open('day12_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    source.append([temp[:1],int(temp[1:])])

ship = [0,0,0]
waypoint = [10,-1]

print(source)

for inst in source:
    if inst[0] == "N":
        waypoint[1] -= inst[1]
    elif inst[0] == "S":
        waypoint[1] += inst[1]
    elif inst[0] == "E":
        waypoint[0] += inst[1]
    elif inst[0] == "W":
        waypoint[0] -= inst[1]
    elif inst[0] == "L":
        turn_step = inst[1] / 90
        if inst[1] % 90 != 0:
            print("Angle error")
            exit()
        turn_step = int(turn_step)
        for i in range(turn_step):
            new_x = waypoint[1]
            new_y = -1 * waypoint[0]
            waypoint = [new_x, new_y]
    elif inst[0] == "R":
        turn_step = inst[1] / 90
        if inst[1] % 90 != 0:
            print("Angle error")
            exit()
        turn_step = int(turn_step)
        for i in range(turn_step):
            new_x = -1 * waypoint[1]
            new_y = waypoint[0]
            waypoint = [new_x, new_y]
    elif inst[0] == "F":
        ship[0] = ship[0] + inst[1] * waypoint[0]
        ship[1] = ship[1] + inst[1] * waypoint[1]
    else:
        print("Instruction error")
        exit()

    print("ship:", ship, "wp:", waypoint)

print(ship)
result = abs(ship[0]) + abs(ship[1])
print("Value of Manhatan distance is:", result)