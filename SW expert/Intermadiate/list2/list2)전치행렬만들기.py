some_list = [[1,2,3],[4,5,6],[7,8,9]]
print(some_list)

# case 1
zip_list = list(zip(*some_list))
print(zip_list)

# case 2
for i in range(len(some_list)):
    for j in range(len(some_list[0])):
        if i < j:
            some_list[i][j], some_list[j][i] = some_list[j][i], some_list[i][j]
print(some_list)

