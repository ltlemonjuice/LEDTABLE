import numpy as np
import time
from matplotlib import pyplot as plt

matrix = [[[0 for x in range(3)] for x in range(10)] for x in range(10)]
#matrix = np.rot90(matrix)
matrix[0][0][0] = 255

def adjustVal():
    for x in range(0, len(matrix)):
        for y in range(0, len(matrix[0])):
            for i in range(0, 3):
                matrix[x][y][i] /= 255


adjustVal()


fig = plt.figure()
arr = plt.imshow(cmatrix, interpolation="nearest")
plt.axis("off")



print(matrix)
matrix[0][1][1] = 255
adjustVal()
print(matrix)

arr.set_data(matrix)
fig.canvas.draw()
plt.show()
