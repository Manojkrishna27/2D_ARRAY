X=[
    [10,9,7], # Subtraction of two matric 
    [9,8,7]
]
Y=[
    [5,6,4], # create two array and one with empty array
    [7,8,3]
]

result=[
    [0,0,0],
    [0,0,0]
]

for i in range(len(X)): # range of rows
    for j in range(len(X[0])):      # range of columns
        result[i][j]=X[i][j]-Y[i][j]             # this line is subtraction logic
print(result)