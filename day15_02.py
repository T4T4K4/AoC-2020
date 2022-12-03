from datetime import datetime

# source = {1:[0,0], 2:[3,0], 3:[6,0]}
start = [15,12,0,14,3,1]
end = 30000000
source = {}
for i in range(1, len(start) + 1):
    source[start[i-1]] = i
counter = len(start)

print(counter)
print(source)

new_number = 0
delta = 0

now = datetime.now()
print(counter, len(source), now.strftime("%H:%M:%S"))

while True:
    counter += 1

    # print(source)

    if new_number in source:
        delta = counter - source[new_number]
    else:
        delta = 0
    
    source[new_number] = counter

    new_number = delta

    # print(source)
    # input("Enter")

    if counter % 100000 == 0:
        now = datetime.now()
        print(counter, len(source), now.strftime("%H:%M:%S"))

    if counter == end - 1:
        break

now = datetime.now()
print(counter, len(source), now.strftime("%H:%M:%S"))

print(len(source))
print(new_number, counter + 1)
print("** konec **")