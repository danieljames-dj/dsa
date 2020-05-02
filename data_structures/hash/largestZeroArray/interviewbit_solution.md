class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return a list of list of integers
    
    def fourSum(self, A, B):
        result = set()
        halfSumList = []
        pairs = {}
        A.sort()
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                sum = A[i] + A[j]
                comp = B - sum
                if comp in pairs:
                    for compPair in pairs[comp]:
                        if compPair[1] < i:
                            result.add((A[compPair[0]], A[compPair[1]], A[i], A[j]))
                if sum not in pairs:
                    pairs[sum] = []
                pairs[sum].append((i, j))
        return sorted([list(item) for item in result])