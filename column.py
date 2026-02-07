matrix=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
rows = len(matrix)
print(rows) # rows
cols = len(matrix[0])
print(cols) # columns
for i in range(rows):
    for j in range(cols):
        print(matrix[j][i],end=" ")
