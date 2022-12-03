file = open('day08_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
for line in lines:
    temp = line.strip("\n")
    temp1 = temp.split(" ")
    temp1.append(0)
    temp1.append(0)
    source.append(temp1)

for i in source:
    print(i)

print()

while True:
    input("waiting....")
    for i in range(len(source)):
         source[i][2] = 0
    pos = 0
    accu = 0
    lock = 0
    while True:
        inst = source[pos][0]
        step = int(source[pos][1])
        print (pos, source[pos], source[3])

        if source[pos][2] == 1:
            print("Loop terminated at instruction", pos, "(row", pos+1, ")")
            print("Infinite loop")
            break

            
        source[pos][2] = 1

        if lock == 1:
            if inst == "nop":
                pos += 1
                print("A")
            elif inst == "acc":
                accu += step
                pos += 1
                print("B")
            elif inst == "jmp":
                pos += step
                print("C")
        
        if lock == 0:
            if inst == "nop" and source[pos][3] == 0:
                source[pos][3] = 1
                pos += step
                lock = 1
                print("D")
            elif inst == "acc":
                accu += step
                pos += 1
                print("E")
            elif inst == "jmp" and source[pos][3] == 0:
                source[pos][3] = 1
                pos += 1
                lock = 1

                print("F")
            elif inst == "nop" and source[pos][3] == 1:
                pos += 1
                print("G")
            elif inst == "jmp" and source[pos][3] == 1:
                pos += step
                print("H")
    
        if pos == len(source):
            print("Program terminated at last instruction", pos, "(row", pos+1, ")")
            print("Accumulator is:", accu)
            exit()
        elif pos > len(source):
            print("Program terminated at high number of instruction")
            break

exit()