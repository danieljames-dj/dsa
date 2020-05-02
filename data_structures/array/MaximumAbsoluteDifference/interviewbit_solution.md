int Solution::maxArr(vector<int> &A) {
    vector<int> positiveGroup, negativeGroup;
    for (int i = 0; i < A.size(); i++) {
        positiveGroup.push_back(A[i] + i);
        negativeGroup.push_back(A[i] - i);
    }
    for (int i = 0; i < A.size(); i++) {
        for (int j = 0; j < A.size(); j++) {
            int y = abs(A[i] - A[j]) + abs(i - j);
            if (y > x) {
                x = y;
            }
        }
    }
    return x;
}