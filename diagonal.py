X=[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]
sum=0
for i in range(len(X)):
    for j in range(len(X[0])):
        if i==j:
            sum+=X[i][i]
print(sum)
