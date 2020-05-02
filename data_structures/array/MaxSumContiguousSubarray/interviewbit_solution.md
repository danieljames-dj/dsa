int Solution::maxSubArray(const vector<int> &A) {
    int bestSum = A[0], sumTillNow = A[0];
    for (int i = 1; i < A.size(); i++) {
        sumTillNow += A[i];
        if (A[i] > sumTillNow) {
            sumTillNow = A[i];
        }
        if (bestSum < sumTillNow) {
            bestSum = sumTillNow;
        }
    }
    return bestSum;
}