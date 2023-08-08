#  nested loops // two dimensional arrays
#  two dimensional array and iterate over that array 
# two dimensional matrix that is square
num= [[1,2,3],[4,5,6],[7,8,9]]
for i in range(len(num)):
    for j in range(len(num[j])):
        print(num[j][i])


# get every pair of elements in array
num = [1,2,3,4,5,6,7,8,9]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        print(num[j],num[i])


# insertion sort
# (insert in middle n times -> n^2)