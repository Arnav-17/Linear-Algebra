import numpy as np
if __name__ == '__main__':
	m = int(input('Enter number of rows\n'))
	a = np.zeros((m,m)) 
	for i in range(m):
		for j in range(m):
			a[i][j] = float(input(f'Enter a{i+1}{j+1}\n'))

def det(l):
	summ = 0
	if len(l) == 1:
		return l[0,0]
	if len(l) > 1:
		for i in range(len(l)):
			b = np.delete(l, 0, 0)
			c = np.delete(b, i, 1)
			y = det(c)*(-1)**i*l[0,i]
			summ += y
		return summ

if __name__ == '__main__':
	print(det(a))