file = open('day03_example.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

tree_matrix = []

for line in lines:
    tree_matrix.append(line[:-1])

rows = len(tree_matrix)
columns = len(tree_matrix[0])

print(rows,columns)

tree_count = 0
j = 0
for i in range(1, rows):
    j = j + 3
    if j > columns - 1:
        j -= columns
    if tree_matrix[i][j] == "#":
        tree_count += 1
    
    print(i,j,tree_matrix[i][j])

print(tree_count)

    
