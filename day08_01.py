file = open('day08_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    temp1 = temp.split(" ")
    temp1.append(0)
    source.append(temp1)

# print(source)

pos = 0
accu = 0
while True:
    inst = source[pos][0]
    step = int(source[pos][1])
    print (inst, step)

    if source[pos][2] == 1:
        print("Program terminate at instruction", pos, "(row", pos+1, ")")
        print("Infinite loop")
        print("Accumulator is:", accu)
        exit()
        
    source[pos][2] = 1
    
    if inst == "nop":
        pos += 1
    elif inst == "acc":
        accu += step
        pos += 1
    elif inst == "jmp":
        pos += step

exit()