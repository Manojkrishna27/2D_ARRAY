X=[          # reverse diagonal view     
    [1,2,3], # create a matrix 
    [4,5,6],
    [7,8,9]
]
n = len(X)      # take range
for i in range(n):           
    print(" "*i, X[i][n - 1 - i]) # first print space and use this reverse logic
