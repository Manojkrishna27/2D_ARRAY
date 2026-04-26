def sum_skip_r_c(arr,r,c):
    total=0
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i!=r and j!=c:
                total+=arr[i][j]
    return total
n=int(input())
arr=[list(map(int,input().split()))for _ in range(n)] # getting input for 2 d array
print(sum_skip_r_c(arr,1,1))