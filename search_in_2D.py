X=[
    [1,2,3],
    [5,4,7],
    [8,7,9]
]

target=3
def search_2d(X,target):
    element=False
    for i in range(len(X)):
       for j in range(len(X[0])):
           if X[i][j]==target:
               element=True
               return element
           else:
              element=False
print(search_2d(X,target))

