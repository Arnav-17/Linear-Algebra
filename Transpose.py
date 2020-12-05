import numpy as np
if __name__ == '__main__':
	m = int(input('Enter number of rows\n'))
	n = int(input('Enter number of columns\n'))
	a = np.zeros((m,n))
	for i in range(m):
		for j in range(n):
			a[i,j] = float(input(f'Enter a{i+1}{j+1}\n'))

def Transpose(l):
	b = np.zeros((len(l),len(l[0])))
	for i in range(len(l)):
		for j in range(len(l[0])):
			b[i,j] = l[j,i]
	return b

if __name__ == '__main__':
	print(Transpose(a))
