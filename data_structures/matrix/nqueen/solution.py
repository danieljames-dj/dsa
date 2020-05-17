def setLocation(mat, row, col, value, validator):
	mat[row][col] = value
	validator[0][col] = value
	validator[1][n-1+col-row] = value
	validator[2][row+col] = value

def isPossible(n, mat, validator, row=0):
	if row == n:
		return True
	for i in range(n):
		if not (validator[0][i] or validator[1][n-1+i-row] or validator[2][row+i]):
			setLocation(mat, row, i, True, validator)
			if isPossible(n, mat, validator, row+1):
				return True
			setLocation(mat, row, i, False, validator)
	return False

n = int(input())
mat = [[False for i in range(n)] for j in range(n)]
validator = [[False for _ in range(2 * n)] for j in range(3)]
isValid = isPossible(n, mat, validator)
if isValid:
	for i in range(n):
		for j in range(n):
			print(1 if mat[i][j] == True else 0, end='\t')
		print('')
else:
	print('IMPOSSIBLE\n')