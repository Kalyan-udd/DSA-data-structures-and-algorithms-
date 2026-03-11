def SpecialPositionBinaryMatrix(mat: list[list[int]]):
    rows = {}
    columns = {}
    m = len(mat)
    n = len(mat[0])
    count = 0
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 1:
                rows[i] = rows.get(i, 0) + 1
                columns[j] = columns.get(j, 0) + 1
    for i in range(m):
        if rows[i] == 1:
            for j in range(n):
                if mat[i][j] == 1:
                    if columns[j] == 1:
                        count += 1
        
    return count
print(SpecialPositionBinaryMatrix(mat = [[1,0,0],[0,1,0],[0,0,1]]))
