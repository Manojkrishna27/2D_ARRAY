X=[
    [1,2,3],  # addition of two matric 
    [4,6,7]
]
            # create two matrics and one empty wuth zero
Y=[
    [8,9,10],
    [5,3,1]
]

result=[
    [0,0,0],
    [0,0,0]
]

for i in range(len(X)): # this is len of rows
    for j in range(len(X[0])): # this is len of columns

        result[i][j]=X[i][j]+Y[i][j]   # row wise addition

print(result)
