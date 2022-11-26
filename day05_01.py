file = open('day05_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

source = []
id=[]
# f=0 b=1 r=1 l=0
for line in lines:
    longtitude = line[:7].strip("\n")
    latitude = line[7:].strip("\n")
    longtitude = longtitude.replace( "B", "1")
    longtitude = longtitude.replace( "F", "0")
    latitude = latitude.replace( "R", "1")
    latitude = latitude.replace( "L", "0")
    lo = int( longtitude, 2 )
    la = int( latitude, 2 )
    source.append([ lo, la, lo * 8 + la ])
    id.append(lo * 8 + la)

id.sort( reverse = True )
print(id[0])


for i, seat in enumerate(id):
    if seat - id[i+1] == 2:
        print(seat, id[i+1])
        break