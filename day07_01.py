file = open('day07_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []

for line in lines[:]:
    temp = line.strip("\n").split("bag")
    
    temp9 = []
    for rule in temp[:-1]:
        temp2 = rule.strip(" ")
        
        # temp3 = temp2.strip("s contain")
        # temp4 = temp3.strip(", ")
        temp9.append(temp2)
    source.append(temp9)
    
colour_list = []
for rule in source:
    if not (rule[0] in colour_list):
        colour_list.append(rule[0])

print("Rule count:", len(source))
print("Colour count:", len(colour_list))

# test funkčnosti databáze
counter = 0
for row in source:
    counter += len(row)
print("Celkem pozic v db:", counter)
print()

# test barevnosti
counter = 0
for i, row in enumerate(source):
    for c in row:
        counter2 = 0
        for col in colour_list:
            if col in c:
                counter += 1
                counter2 += 1
        # if counter2 == 0:
            # print("Vadný řádek:", i, row)
 
for i, row in enumerate(source):
    if "shiny gold" in row[0]:
        print(i, row)

print("Celkem barevných pozic v db:", counter)
print()

def multiply_color(xxx):
    x_list = []
    for rule in source: # základní seznam všech pravidel
        for c in rule[1:]:
            if xxx in c:
                x_list.append(rule)
    xxx_list = []
    for row in x_list:
        xxx_list.append(row[0])
    return(xxx_list)

# první kolo výběru
xxx = "shiny gold"
selected_color = [multiply_color(xxx)]

print("Počet rules pro barvu:", "-" + xxx + "-", "je", len(selected_color[0]))
for i in selected_color[0]:
    print(i)
print()

for iii in range(15):
    selected = []
    for row in selected_color[-1]: # vyber z posledního přidaného seznamu [-1] postupně barvy nebo [část]
        # print("* Multiply this:",row)
        selected.append(multiply_color(row))
        # for col in selected[-1]:
            # print(col)
    print()
    joined_selected = [x for l in selected for x in l]
    # for col in joined_selected:
        # print(col)
    print("(1) Délka joined selected created:", len(joined_selected))

    # porovnání starých seznamů s novým
    tlist = joined_selected.copy()
    for ii in range(iii+1):
        for col1 in selected_color[ii]:
            for j, col2 in enumerate(tlist): # copy of joined selected
                if col1 == col2:
                    print(col2)
                    joined_selected.remove(col2)
        print("(2) Délka joined selected:", len(joined_selected))
    
    # porovnání nového seznamu se sebou (nalezení duplicit)
    tlist = joined_selected.copy()
    for i, col1 in enumerate(tlist):
        for col2 in tlist[i+1:]:
            if col1 == col2:
                print(col1)
                joined_selected.remove(col2)

    print("(3) Délka joined selected:", len(joined_selected))
    selected_color.append(joined_selected)
    

    print("Nový seznam připojen. Délky jednotlivých seznamů:")
    counter = 0
    for i in selected_color:
        counter += len(i)
        print(len(i), end = " ")
    print()
    print("Celkem barev ze shiny gold pytlem:", counter)
    