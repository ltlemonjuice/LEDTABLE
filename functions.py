
def allocate(matrix):
    cmatrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
    for x in range(0,10):
        for y in range (0,10):
            cmatrix[x][y][0] = matrix[x][y][0]
            cmatrix[x][y][1] = matrix[x][y][1]
            cmatrix[x][y][2] = matrix[x][y][2]

            #Column 1
            col = 1
            if x == col and y == 0:
                cmatrix[x][y][0] = matrix[col][9][0]
                cmatrix[x][y][1] = matrix[col][9][1]
                cmatrix[x][y][2] = matrix[col][9][2]
            elif x == col and y == 1:
                cmatrix[x][y][0] = matrix[col][8][0]
                cmatrix[x][y][1] = matrix[col][8][1]
                cmatrix[x][y][2] = matrix[col][8][2]
            elif x == col and y == 2:
                cmatrix[x][y][0] = matrix[col][7][0]
                cmatrix[x][y][1] = matrix[col][7][1]
                cmatrix[x][y][2] = matrix[col][7][2]
            elif x == col and y == 3:
                cmatrix[x][y][0] = matrix[col][6][0]
                cmatrix[x][y][1] = matrix[col][6][1]
                cmatrix[x][y][2] = matrix[col][6][2]
            elif x == col and y == 4:
                cmatrix[x][y][0] = matrix[col][5][0]
                cmatrix[x][y][1] = matrix[col][5][1]
                cmatrix[x][y][2] = matrix[col][5][2]
            elif x == col and y == 5:
                cmatrix[x][y][0] = matrix[col][4][0]
                cmatrix[x][y][1] = matrix[col][4][1]
                cmatrix[x][y][2] = matrix[col][4][2]
            elif x == col and y == 6:
                cmatrix[x][y][0] = matrix[col][3][0]
                cmatrix[x][y][1] = matrix[col][3][1]
                cmatrix[x][y][2] = matrix[col][3][2]
            elif x == col and y == 7:
                cmatrix[x][y][0] = matrix[col][2][0]
                cmatrix[x][y][1] = matrix[col][2][1]
                cmatrix[x][y][2] = matrix[col][2][2]
            elif x == col and y == 8:
                cmatrix[x][y][0] = matrix[col][1][0]
                cmatrix[x][y][1] = matrix[col][1][1]
                cmatrix[x][y][2] = matrix[col][1][2]
            elif x == col and y == 9:
                cmatrix[x][y][0] = matrix[col][0][0]
                cmatrix[x][y][1] = matrix[col][0][1]
                cmatrix[x][y][2] = matrix[col][0][2]

            #Column 3
            col = 3
            if x == col and y == 0:
                cmatrix[x][y][0] = matrix[col][9][0]
                cmatrix[x][y][1] = matrix[col][9][1]
                cmatrix[x][y][2] = matrix[col][9][2]
            elif x == col and y == 1:
                cmatrix[x][y][0] = matrix[col][8][0]
                cmatrix[x][y][1] = matrix[col][8][1]
                cmatrix[x][y][2] = matrix[col][8][2]
            elif x == col and y == 2:
                cmatrix[x][y][0] = matrix[col][7][0]
                cmatrix[x][y][1] = matrix[col][7][1]
                cmatrix[x][y][2] = matrix[col][7][2]
            elif x == col and y == 3:
                cmatrix[x][y][0] = matrix[col][6][0]
                cmatrix[x][y][1] = matrix[col][6][1]
                cmatrix[x][y][2] = matrix[col][6][2]
            elif x == col and y == 4:
                cmatrix[x][y][0] = matrix[col][5][0]
                cmatrix[x][y][1] = matrix[col][5][1]
                cmatrix[x][y][2] = matrix[col][5][2]
            elif x == col and y == 5:
                cmatrix[x][y][0] = matrix[col][4][0]
                cmatrix[x][y][1] = matrix[col][4][1]
                cmatrix[x][y][2] = matrix[col][4][2]
            elif x == col and y == 6:
                cmatrix[x][y][0] = matrix[col][3][0]
                cmatrix[x][y][1] = matrix[col][3][1]
                cmatrix[x][y][2] = matrix[col][3][2]
            elif x == col and y == 7:
                cmatrix[x][y][0] = matrix[col][2][0]
                cmatrix[x][y][1] = matrix[col][2][1]
                cmatrix[x][y][2] = matrix[col][2][2]
            elif x == col and y == 8:
                cmatrix[x][y][0] = matrix[col][1][0]
                cmatrix[x][y][1] = matrix[col][1][1]
                cmatrix[x][y][2] = matrix[col][1][2]
            elif x == col and y == 9:
                cmatrix[x][y][0] = matrix[col][0][0]
                cmatrix[x][y][1] = matrix[col][0][1]
                cmatrix[x][y][2] = matrix[col][0][2]

            #Column 5
            col = 5
            if x == col and y == 0:
                cmatrix[x][y][0] = matrix[col][9][0]
                cmatrix[x][y][1] = matrix[col][9][1]
                cmatrix[x][y][2] = matrix[col][9][2]
            elif x == col and y == 1:
                cmatrix[x][y][0] = matrix[col][8][0]
                cmatrix[x][y][1] = matrix[col][8][1]
                cmatrix[x][y][2] = matrix[col][8][2]
            elif x == col and y == 2:
                cmatrix[x][y][0] = matrix[col][7][0]
                cmatrix[x][y][1] = matrix[col][7][1]
                cmatrix[x][y][2] = matrix[col][7][2]
            elif x == col and y == 3:
                cmatrix[x][y][0] = matrix[col][6][0]
                cmatrix[x][y][1] = matrix[col][6][1]
                cmatrix[x][y][2] = matrix[col][6][2]
            elif x == col and y == 4:
                cmatrix[x][y][0] = matrix[col][5][0]
                cmatrix[x][y][1] = matrix[col][5][1]
                cmatrix[x][y][2] = matrix[col][5][2]
            elif x == col and y == 5:
                cmatrix[x][y][0] = matrix[col][4][0]
                cmatrix[x][y][1] = matrix[col][4][1]
                cmatrix[x][y][2] = matrix[col][4][2]
            elif x == col and y == 6:
                cmatrix[x][y][0] = matrix[col][3][0]
                cmatrix[x][y][1] = matrix[col][3][1]
                cmatrix[x][y][2] = matrix[col][3][2]
            elif x == col and y == 7:
                cmatrix[x][y][0] = matrix[col][2][0]
                cmatrix[x][y][1] = matrix[col][2][1]
                cmatrix[x][y][2] = matrix[col][2][2]
            elif x == col and y == 8:
                cmatrix[x][y][0] = matrix[col][1][0]
                cmatrix[x][y][1] = matrix[col][1][1]
                cmatrix[x][y][2] = matrix[col][1][2]
            elif x == col and y == 9:
                cmatrix[x][y][0] = matrix[col][0][0]
                cmatrix[x][y][1] = matrix[col][0][1]
                cmatrix[x][y][2] = matrix[col][0][2]

            #Column 7
            col = 7
            if x == col and y == 0:
                cmatrix[x][y][0] = matrix[col][9][0]
                cmatrix[x][y][1] = matrix[col][9][1]
                cmatrix[x][y][2] = matrix[col][9][2]
            elif x == col and y == 1:
                cmatrix[x][y][0] = matrix[col][8][0]
                cmatrix[x][y][1] = matrix[col][8][1]
                cmatrix[x][y][2] = matrix[col][8][2]
            elif x == col and y == 2:
                cmatrix[x][y][0] = matrix[col][7][0]
                cmatrix[x][y][1] = matrix[col][7][1]
                cmatrix[x][y][2] = matrix[col][7][2]
            elif x == col and y == 3:
                cmatrix[x][y][0] = matrix[col][6][0]
                cmatrix[x][y][1] = matrix[col][6][1]
                cmatrix[x][y][2] = matrix[col][6][2]
            elif x == col and y == 4:
                cmatrix[x][y][0] = matrix[col][5][0]
                cmatrix[x][y][1] = matrix[col][5][1]
                cmatrix[x][y][2] = matrix[col][5][2]
            elif x == col and y == 5:
                cmatrix[x][y][0] = matrix[col][4][0]
                cmatrix[x][y][1] = matrix[col][4][1]
                cmatrix[x][y][2] = matrix[col][4][2]
            elif x == col and y == 6:
                cmatrix[x][y][0] = matrix[col][3][0]
                cmatrix[x][y][1] = matrix[col][3][1]
                cmatrix[x][y][2] = matrix[col][3][2]
            elif x == col and y == 7:
                cmatrix[x][y][0] = matrix[col][2][0]
                cmatrix[x][y][1] = matrix[col][2][1]
                cmatrix[x][y][2] = matrix[col][2][2]
            elif x == col and y == 8:
                cmatrix[x][y][0] = matrix[col][1][0]
                cmatrix[x][y][1] = matrix[col][1][1]
                cmatrix[x][y][2] = matrix[col][1][2]
            elif x == col and y == 9:
                cmatrix[x][y][0] = matrix[col][0][0]
                cmatrix[x][y][1] = matrix[col][0][1]
                cmatrix[x][y][2] = matrix[col][0][2]

            #Column 9
            col = 9
            if x == col and y == 0:
                cmatrix[x][y][0] = matrix[col][9][0]
                cmatrix[x][y][1] = matrix[col][9][1]
                cmatrix[x][y][2] = matrix[col][9][2]
            elif x == col and y == 1:
                cmatrix[x][y][0] = matrix[col][8][0]
                cmatrix[x][y][1] = matrix[col][8][1]
                cmatrix[x][y][2] = matrix[col][8][2]
            elif x == col and y == 2:
                cmatrix[x][y][0] = matrix[col][7][0]
                cmatrix[x][y][1] = matrix[col][7][1]
                cmatrix[x][y][2] = matrix[col][7][2]
            elif x == col and y == 3:
                cmatrix[x][y][0] = matrix[col][6][0]
                cmatrix[x][y][1] = matrix[col][6][1]
                cmatrix[x][y][2] = matrix[col][6][2]
            elif x == col and y == 4:
                cmatrix[x][y][0] = matrix[col][5][0]
                cmatrix[x][y][1] = matrix[col][5][1]
                cmatrix[x][y][2] = matrix[col][5][2]
            elif x == col and y == 5:
                cmatrix[x][y][0] = matrix[col][4][0]
                cmatrix[x][y][1] = matrix[col][4][1]
                cmatrix[x][y][2] = matrix[col][4][2]
            elif x == col and y == 6:
                cmatrix[x][y][0] = matrix[col][3][0]
                cmatrix[x][y][1] = matrix[col][3][1]
                cmatrix[x][y][2] = matrix[col][3][2]
            elif x == col and y == 7:
                cmatrix[x][y][0] = matrix[col][2][0]
                cmatrix[x][y][1] = matrix[col][2][1]
                cmatrix[x][y][2] = matrix[col][2][2]
            elif x == col and y == 8:
                cmatrix[x][y][0] = matrix[col][1][0]
                cmatrix[x][y][1] = matrix[col][1][1]
                cmatrix[x][y][2] = matrix[col][1][2]
            elif x == col and y == 9:
                cmatrix[x][y][0] = matrix[col][0][0]
                cmatrix[x][y][1] = matrix[col][0][1]
                cmatrix[x][y][2] = matrix[col][0][2]

            cmatrix.reverse()
            return cmatrix
