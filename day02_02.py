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
    print(psw[0], psw[1], psw[3])
    print(psw[3][psw[0]-1], psw[3][psw[1]-1])
    
    if len(psw[3]) >= psw[1]:
        aaa = 0
        bbb = 0
        if psw[2] == psw[3][psw[0]-1]:
            aaa = 1
        if psw[2] == psw[3][psw[1]-1]:
            bbb = 1

        if aaa + bbb == 1:
            source[i].append("true")
            counter_psw += 1

print(counter_psw)