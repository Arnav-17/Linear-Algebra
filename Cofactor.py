import numpy as np
from Determinant import det
if __name__ == '__main__':
	m = int(input('Enter number of rows\n'))
	a = np.zeros((m,m)) 
	for i in range(m):
		for j in range(m):
			a[i][j] = float(input(f'Enter a{i+1}{j+1}\n'))


def cofac(l,x, y):
	b = np.delete(l, x, 0)
	c = np.delete(b, y, 1)
	return det(c)


def cofacmatrix(d):
	k = np.zeros((len(d), len(d)))
	for i in range(len(d)):
		for j in range(len(d)):
			k[i,j] = (-1)**(i+j)*cofac(d, i, j)
	return k

if __name__ == '__main__':
	print(cofacmatrix(a))
	