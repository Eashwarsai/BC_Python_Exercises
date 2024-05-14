import numpy as np 
matrix_1= np.arange(6).reshape(3, 2)
matrix_2 = np.ones((2, 2), dtype=int)
matrix_1 @= matrix_2
print(matrix_2)