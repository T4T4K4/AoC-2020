import numpy

file = open('day03_source.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

slope_matrix = [[1,1],[3,1],[5,1],[7,1],[1,2]]
tree_matrix = []

for line in lines:
    tree_matrix.append(line[:-1])

rows = len(tree_matrix)
columns = len(tree_matrix[0])

print(rows,columns)

tree_count_list = []


for horse in slope_matrix:
    tree_count = 0
    j = 0
    for i in range( horse[1], rows, horse[1] ):
        j = j + horse[0]
        if j > columns - 1:
            j -= columns
        if tree_matrix[i][j] == "#":
            tree_count += 1
        
        # print(i,j,tree_matrix[i][j])
    tree_count_list.append(tree_count)
    print()

print(tree_count_list)
print(numpy.prod(tree_count_list))

    
