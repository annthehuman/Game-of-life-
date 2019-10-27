import numpy as np
import copy

def pprint(a):
	for i in range (n):
		for j in range (m):
			if a[i][j] == 0:
				print('.', end = '')
			if a[i][j] == 1:
				print('*', end = '')
		print()
	print()

n, m, k = (int(i) for i in input().split()) #чтение размеров поля и числа начальных клеток
a = [[0 for j in range(m)] for i in range(n)]
s = [[0 for j in range(m)] for i in range(n)]
storage = {}
v = 0 
for i in range(k):
	row, col = (int(i) for i in input().split())
	a[row][col] = 1 #расставляем начальные клетки

pprint(a)

while np.sum(a) != 0:
	for i in range(n):
		for j in range(m):
			summa = 0
			if a[i][j] == 0:  # в этой клетке жизни нет, считаем число жизней вокруг, если их 3, в клетке зарождается жизнь
				for di in range(-1, 2):
					for dj in range(-1, 2):
						ai = i + di
						aj = j + dj
						if 0 <= ai < n and 0 <= aj < m:
							summa += a[ai][aj]
							if summa == 3:
								s[i][j] = 1

	for i in range(n):
		for j in range(m):
			if a[i][j] == 1:  # в этой клетке жизнь есть, считаем число жизней вокругб если их меньше 2 или больше 3, клетка умирает
				a[i][j] = 0
				summa = 0
				for di in range(-1, 2):
					for dj in range(-1, 2):
						ai = i + di
						aj = j + dj
						if 0 <= ai < n and 0 <= aj < m:
							summa += a[ai][aj]
							if 2 <= summa <= 3:
								s[i][j] = 1
							else:
								s[i][j] = 0
				a[i][j] = 1
	if a in storage.values():
		break
	else:
		storage[v] = s
		v += 1
		a = copy.deepcopy(s)
	pprint(s)
