def sortMatrix(matrix):
    # matrix.sort(key=sum)
    sorted_matrix=sorted(matrix,key=sum)
    return sorted_matrix

matrix=[[5,6,2],[3,1,2],[1,2,3],[4,2,1]]
print(sortMatrix(matrix))
# print(matrix)


