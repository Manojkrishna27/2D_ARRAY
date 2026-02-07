X=[
    [1,2,3],    # createa 2d Array now we are going to make diagonal view of Array
    [4,5,6],
    [7,8,9]
]

for i in range(len(X)):         # rows
    for j in range(len(X[i])):   # columns
        if i==j:                   # main diagonal logic 
            print(X[i][j],end=" ")               # print
        else:
            print(" ",end=" ")                   # else space
    print()                                  # this print is for exit the j iteration
           