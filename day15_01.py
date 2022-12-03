# example
source = [15,12,0,14,3,1]
lenght = len(source)

for nn in range(2020 - lenght):
    last = source[-1]
    if last not in source[:-1]:
        source.append(0)

    else:
        lock = 0
        lenght = len(source)
        for i in range(lenght - 2, -1, -1):
            if source[i] == last:
                # print(lenght, i)
                source.append(lenght - i - 1)
                break

print(source[-1])