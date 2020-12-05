import numpy as np
from Determinant import det
from Transpose import Transpose
from Cofactor import cofacmatrix
from Inverse import inverse
from Matmultiply import matmult
r = input('T for Transpose, I for inverse, D for Determinant, C for Cofactor matrix, M for Matrix multiplication\n')


if r == 'M':
	print('Enter elements of 1st matrix')
	m = int(input('Enter number of rows\n'))
	n = int(input('Enter number of columns\n'))
	a = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			a[i,j] = float(input(f'Enter a{i+1}{j+1}\n'))
	print('Enter elements of 2nd matrix')
	p = int(input('Enter number of rows\n'))
	q = int(input('Enter number of columns\n'))
	b = np.zeros((p,q))
	for i in range(p):
		for j in range(q):
			b[i,j] = float(input(f'Enter b{i+1}{j+1}\n'))
	print(matmult(a,b))

elif r == 'T':
	m = int(input('Enter number of rows\n'))
	n = int(input('Enter number of columns\n'))
	a = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			a[i,j] = float(input(f'Enter a{i+1}{j+1}\n'))
	print(Transpose(a))

elif r == 'I':
	m = int(input('Enter number of rows\n'))
	a = np.zeros((m,m))
	for i in range(m):
		for j in range(m):
			a[i,j] = float(input(f'Enter a{i+1}{j+1}\n'))
	print(inverse(a))


elif r == 'D':
	m = int(input('Enter number of rows\n'))
	a = np.zeros((m,m))
	for i in range(m):
		for j in range(m):
			a[i,j] = float(input(f'Enter a{i+1}{j+1}\n'))
	print(det(a))

elif r == 'C':
	m = int(input('Enter number of rows\n'))
	a = np.zeros((m,m))
	for i in range(m):
		for j in range(m):
			a[i,j] = float(input(f'Enter a{i+1}{j+1}\n'))
	print(cofacmatrix(a))