def numberOfDeletions(string, matrix, start, end):
	if matrix[start][end] != -1:
		return matrix[start][end]
	elif end - start <= 1:
		matrix[start][end] = 0
	elif string[start] == string[end-1]:
		matrix[start][end] = numberOfDeletions(string, matrix, start+1, end-1)
	else:
		matrix[start][end] = 1 + min(numberOfDeletions(string, matrix, start+1, end), numberOfDeletions(string, matrix, start, end-1))
	return matrix[start][end]

string = input()
matrix = [[-1 for i in range(len(string)+1)] for j in range(len(string)+1)]
print(numberOfDeletions(string, matrix, 0, len(string)))