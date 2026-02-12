X=[
    [1,2,3],
    [4,5,6],
    [7,1,2]
]
sum=0
total_sum=0
for i in range(len(X)):
    for j in range(len(X[0])):
        sum+=X[i][j]
        if sum>total_sum:
            total_sum=sum
            sum=0
        
        
print(total_sum)
