import numpy as np
from Determinant import det
from Transpose import Transpose
from Cofactor import cofacmatrix
if __name__ == '__main__':
	m = int(input('Enter number of rows\n'))
	a = np.zeros((m,m))
	for i in range(m):
		for j in range(m):
			a[i][j] = float(input(f'Enter a{i+1}{j+1}\n'))

def inverse(l):
	return Transpose(cofacmatrix(l))/det(l)

if __name__ == '__main__':
	print(inverse(a))