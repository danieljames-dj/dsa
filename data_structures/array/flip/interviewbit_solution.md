vector<int> Solution::flip(string A) {
    int bestStart = -1, bestEnd = -1, bestSum = 0, curStart = 0, curEnd = 0, curSum = 0;
    vector<int> solution;
    for (int i = 0; i < A.size(); i++) {
        int curValue = (A[i] == '0' ? 1 : -1);
        if (curValue > curValue + curSum) {
            curStart = curEnd = i;
            curSum = curValue;
        } else {
            curSum += curValue;
            curEnd = i;
        }
        curEnd = i;
        if (curSum > bestSum) {
            bestSum = curSum;
            bestStart = curStart;
            bestEnd = curEnd;
        }
    }
    if (bestStart == -1) {
        return solution;
    } else {
        solution.push_back(bestStart + 1);
        solution.push_back(bestEnd + 1);
        return solution;
    }
}