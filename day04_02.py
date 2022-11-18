file = open('day04_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.read()
file.close()

source = []
temp = lines.split("\n\n")
for pas_tmp in temp:
    pas_tmp_splitted = []
    pas_rows_temp = pas_tmp.split("\n")
    for pas_row_temp in pas_rows_temp:
        fields = pas_row_temp.split(" ")
        for field in fields:
            pas_tmp_splitted.append(field)
    source.append(pas_tmp_splitted)

# make dictionary
source_d = []
for pas in source:
    pas_d = dict(x.split(":") for x in pas)
    source_d.append(pas_d)

# save memory
source = []

fields = [["byr", 1920, 2002], ["iyr", 2010, 2020], ["eyr", 2020, 2030],
["hgt", 150, 193, 59, 76], ["hcl", "#0123456789abcdef"],
["ecl", "amb", "blu", "brn", "gry", "grn", "hzl", "oth"],
["pid", "0123456789"], ["cid"]]

pas_valid = []

for pas in source_d:
    counter = 0
    for key, val in pas.items():
        if key == "byr":
            if 1920 <= int(val) <= 2002:
                # print(1, end = "")
                counter += 1
        if key == "iyr":
            if 2010 <= int(val) <= 2020:
                # print(2, end = "")
                counter += 1
        if key == "eyr":
            if 2020 <= int(val) <= 2030:
                # print(3, end = "")
                counter += 1
        if key == "hgt":
            if val[-2:] == "cm":
                if 150 <= int(val[:-2]) <= 193:
                    # print("4a", end = "")
                    counter += 1
            elif val[-2:] == "in":
                if 59 <= int(val[:-2]) <= 76:
                    # print("4b", end = "")
                    counter += 1
        if key == "hcl" and val[0] == "#" and len(val) == 7:
            c7 = 0
            for ltr in val:
                if ltr in "#0123456789abcdef":
                    c7 += 1
            if c7 == 7:
                # print(5, end = "")
                counter += 1
        if key == "ecl":
            if val in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]:
                # print(6, end = "")
                counter += 1
        if key == "pid" and len(val) == 9:
            c9 = 0
            for ltr in val:
                if ltr in "0123456789":
                    c9 += 1
            if c9 == 9:
                # print(7, end = "")
                counter += 1
    
    # print(" *",counter)
    
    if counter == 7:
        pas_valid.append(1)
    else:
        pas_valid.append(0)

# print(pas_valid)
print(sum(pas_valid))


        


