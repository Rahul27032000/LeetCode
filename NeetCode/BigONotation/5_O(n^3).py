# its pretty uncommon to have this much time complexity

# get every triplet of element in array
num = [1,2,3]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        for k in range(j+1,len(num)):
            print(num[i],num[j],num[k])