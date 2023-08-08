#  O(n*m)
# two dimensional matrix that is not  a square
# let every pair of element from two arrays
num1,num2=[1,2,3][1,2]
for i in range(len(num1)):
    for j in range(len(num2)):
        print(num1[i], num2[j])

# traverse rectangle grid
num3 = [[1,2,3],[4,5,6]]
for i in range(len(num3)):
    for j in range(len(num3[i])):
        print(num3[i][j])