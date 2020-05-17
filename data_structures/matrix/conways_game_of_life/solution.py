def compute(matrix, sr, sc, er, ec):
	for i in range(max(0, sr-1), er+2):
		for j in range(max(0, sc-1), ec+2):
			nc = 0
			for ii in range(-1, 2):
				for jj in range(-1, 2):
					if ii + i >= max(0, sr-1) and ii + i <= er+1 \
					and jj + j >= max(0, sc-1) and jj + j <= ec+1 \
					and not (ii == 0 and jj == 0) and matrix[ii+i][jj+j] % 2 == 1:
						nc += 1
			if nc == 2:
				matrix[i][j] = (matrix[i][j] << 1) + matrix[i][j]
			if nc == 3:
				matrix[i][j] += 2
	for i in range(max(0, sr-1), er+2):
		for j in range(max(0, sc-1), ec+2):
			matrix[i][j] = matrix[i][j] >> 1

n = int(input())
live_cells = []
sr = 1000
sc = 1000
er = 0
ec = 0
for _ in range(n):
	cell = [int(i) for i in input().split()]
	sr = min(sr, cell[0])
	sc = min(sc, cell[1])
	er = max(er, cell[0])
	ec = max(ec, cell[1])
	live_cells.append(cell)
steps = int(input())
matrix = [[0 for i in range(ec+2)] for j in range(er+2)]
for cell in live_cells:
	matrix[cell[0]][cell[1]] = 1
for _ in range(steps):
	compute(matrix, sr, sc, er, ec)
for i in range(len(matrix)):
	print(matrix[i])