import math

file = open('day13_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

timestamp = int(lines[0].strip("\n"))

temp = lines[1].strip("\n")
temp1 = temp.split(",")

print(temp1)

source = []
for i in range(len(temp1)):
    if temp1[i] != "x":
        source.append([i,int(temp1[i])])

# source.sort(key=lambda x: x[1], reverse=True)
print(source)

step = 1
counter = 1
for i in range(1, len(source)):

    while True:
        ref_val = counter * source[0][1]
        delay = source[i][0]
        comp_val = math.ceil((ref_val + delay) / source [i][1]) * source[i][1]

        if comp_val - ref_val == delay:
            
            step *= source[i][1]
            print("OK", counter, step)
            print(ref_val, comp_val)

            break

        # input("enter to continue")
        counter += step


print("** konec **")
