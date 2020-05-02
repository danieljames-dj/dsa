int Solution::isPalindrome(string A) {
    int start = 0, end = A.length() - 1;
    while (1) {
        while (start <= end && !isalnum(A[start])) {
            start++;
        }
        while (start <= end && !isalnum(A[end])) {
            end--;
        }
        if (start >= end) {
            return 1;
        } else if (tolower(A[start]) != tolower(A[end])) {
            return 0;
        }
        start++;
        end--;
    }
    return 1;
}