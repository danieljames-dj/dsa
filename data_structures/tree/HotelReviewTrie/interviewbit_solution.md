struct node {
    bool isEnd;
    struct node *children[26];
};

struct node* createNode() {
    struct node *el = new struct node;
    el -> isEnd = false;
    for (int i = 0; i < 26; i++) {
        el -> children[i] = NULL;
    }
    return el;
}

void insert(struct node *ptr, string x) {
    if (x.length() && islower(x[0])) {
        int index = x[0] - 'a';
        if (!(ptr -> children[index])) {
            ptr -> children[index] = createNode();
        }
        ptr = ptr -> children[index];
        insert(ptr, x.substr(1, x.length() - 1));
    } else {
        ptr -> isEnd = true;
    }
}

bool isPresent(struct node *ptr, string x) {
    for (int i = 0; i < x.length(); i++) {
        ptr = ptr -> children[x[i] - 'a'];
        if (!ptr) {
            return false;
        }
    }
    return ptr -> isEnd;
}

int getWordEnd(string str, int start) {
    while (start < str.length() && islower(str[start])) {
        start++;
    }
    return start;
}

vector<int> Solution::solve(string A, vector<string> &B) {
    struct node *root = createNode();
    vector<int> result(B.size(), -1);
    vector<int> freq(B.size(), 0);
    int start = 0, end;
    while (start < A.length()) {
        end = getWordEnd(A, start);
        insert(root, A.substr(start, end - start));
        start = end + 1;
    }
    for (int i = 0; i < B.size(); i++) {
        start = 0;
        int count = 0;
        while (start < B[i].length()) {
            end = getWordEnd(B[i], start);
            if (isPresent(root, B[i].substr(start, end - start))) {
                count++;
            }
            start = end + 1;
        }
        freq[i] = count;
        int k = i;
        for (int j = i-1; j >= 0; j--) {
            if (freq[result[j]] < freq[i]) {
                result[j+1] = result[j];
                k--;
            } else {
                break;
            }
        }
        result[k] = i;
    }
    return result;
}
