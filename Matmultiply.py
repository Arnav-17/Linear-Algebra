import numpy as np
if __name__ == '__main__':
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

def matmult(r,s):
	x = []
	y = []
	u = []
	v = np.zeros((1,len(r)*len(s[0])))
	for i in range(len(r)):
		x.append(r[i])
	for i in range(len(s[0])):
		y.append(s[:,i])
	for i in range(len(r)):
		for j in range(len(s[0])):
			c = x[i]*y[j]
			u.append(c)		
	for i in range(len(r)*len(s[0])):
		z = sum(u[i])
		v[0,i] = z
	t = v.reshape(len(r), len(s[0]))
	return t

if __name__ == '__main__':
	print(matmult(a,b))