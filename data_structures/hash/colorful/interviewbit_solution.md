C++ solution:

int Solution::colorful(int A) {
    unordered_map<long long, bool> umap;
    string num = to_string(A);
    long long mul;
    for (int i = 0; i < num.length(); i++) {
        mul = 1;
        for (int j = i; j < num.length(); j++) {
            mul *= (num[j] - '0');
            if (umap.find(mul) == umap.end()) {
                umap[mul] = true;
            } else {
                return 0;
            }
        }
    }
    return 1;
}

Python solution:

class Solution:
    # @param A : integer
    # @return an integer
    def colorful(self, A):
        prod = {}
        digits = []
        while A > 0:
            digits.append(A%10)
            A = A/10
        for i in range(0, len(digits)):
            curProd = 1
            for j in range(i, len(digits)):
                curProd *= digits[j]
                if (prod.has_key(curProd)):
                    return 0
                prod[curProd] = 1
        return 1