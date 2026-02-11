X=[
    [1,0,0], # checking this identity matrix
    [0,1,0],
    [0,0,1]
]
identity=True      # take as true
for i in range(len(X)):     # len of rows
    for j in range(len(X[0])): # len of columns
        if i==j: # this if for diagonal
            if X[i][j]!=1:   # checking not equal to 1
                identity=False
                break
        else:
             if X[i][j]!=0:   # checkint not equal to 0
                 identity=False
                 break
print(identity)

                
