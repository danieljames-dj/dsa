vector<vector<int> > Solution::generateMatrix(int A) {
    vector<vector<int>> result(A, vector<int>(A, 0));
    int i = 0, j = 0, n = 1;
    while (n <= pow(A, 2)) {
        while (j < A && result[i][j] == 0) {
            result[i][j++] = n++;
        }
        j--;
        i++;
        while (i < A && result[i][j] == 0) {
            result[i++][j] = n++;
        }
        i--;
        j--;
        while (j >= 0 && result[i][j] == 0) {
            result[i][j--] = n++;
        }
        j++;
        i--;
        while (i >= 0 && result[i][j] == 0) {
            result[i--][j] = n++;
        }
        i++;
        j++;
    }
    return result;
}