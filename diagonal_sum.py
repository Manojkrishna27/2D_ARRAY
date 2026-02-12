X=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sum=0 # take as 0
for i in range(len(X)): # len of Rows
    for j in range(len(X[0])): # len of columns 
        if i==j:       # condition for diagonal
            sum+=X[i][i]      # adding each
print(sum)
