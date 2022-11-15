file = open('day02_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()
source = []

for line in lines:
    temp1 = line.split(" ")
    ll = int((temp1[0].split("-"))[0])
    lh = int((temp1[0].split("-"))[1])
    ltr = temp1[1][0]
    strg = temp1[2][:-1]
    source.append( [ ll, lh, ltr, strg ] )

counter_psw = 0
for i, psw in enumerate(source):
    counter = 0
    for ltr in psw[3]:
        if ltr == psw[2]:
            counter += 1
    source[i].append(counter)
    if psw[0] <= counter <= psw[1]:
        source[i].append("true")
        counter_psw += 1
    else:
        source[i].append("false")

print(counter_psw)